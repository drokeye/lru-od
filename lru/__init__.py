"""
lru-od - LRU Cache implementation in python using ordered-dict
"""

import typing as t
from collections import OrderedDict

__all__ = ("LRUCache",)
__version__ = "0.0.1"
__author__ = "XiehCanCode"


KT = t.TypeVar("KT")
VT = t.TypeVar("VT")


class LRUCache(t.Generic[KT, VT]):
    """LRUCache implementation

    Parameters
    ----------
    max_size: Optional[:class:`int`]
        Max size of the cache, default is 120
    """

    __slots__ = ("max_size", "_cache", "hits", "miss", "current_size")

    def __init__(self, max_size: int = 120):
        self.max_size = max_size
        self._cache: OrderedDict[KT, VT] = OrderedDict()
        self.hits = 0
        self.miss = 0
        self.current_size = 0

    def __contains__(self, o: object) -> bool:
        return self._cache.__contains__(o)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, LRUCache) and self._cache == o._cache  # type: ignore

    def __getitem__(self, key: KT) -> VT:
        get = self._cache.get(key)
        if not get:
            raise KeyError
        self._cache.move_to_end(key)
        return get

    def __iter__(self) -> t.Iterator[KT]:
        return self._cache.__iter__()

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __repr__(self) -> str:
        return f"<LRUCache max_size={self.max_size} current_size={self.current_size} hits={self.hits} miss={self.miss}>"

    def __setitem__(self, key: KT, value: VT) -> None:
        if len(self._cache) >= self.max_size:
            self._cache.popitem(last=False)
            self.current_size -= 1
            self._cache[key] = value
            self._cache.move_to_end(key)
            self.current_size += 1
        self._cache[key] = value
        self._cache.move_to_end(key)
        self.current_size += 1

    def cache_info(self) -> str:
        """Information about the cache"""
        return f"<hits={self.hits} miss={self.miss} current_size={self.current_size} max_size={self.max_size}>"

    def get(self, key: KT) -> t.Union[VT, None]:
        """Get a value of the key-value pair with given `key` if exists

        Parameters
        ----------
        key: Any
            The key associated with the pair
        """
        value = self._cache.get(key)
        if not value:
            self.miss += 1
            return None
        self.hits += 1
        self._cache.move_to_end(key)
        return value

    def items(self) -> t.ItemsView[KT, VT]:
        """D.values() -> a set-like object providing a view on D's items"""
        return self._cache.items()

    def keys(self) -> t.KeysView[KT]:
        """D.keys() -> a set-like object providing a view on D's keys"""
        return self._cache.keys()

    def remove(self, key: KT) -> None:
        """Remove a key-value pair associated with the `key` parameter

        Parameters
        ----------
        key: Any
            The key associated with the pair

        Raises
        ------
        KeyError: If you're trying to delete a key-value pair which is not in the cache
        """
        del self._cache[key]

    def set(self, key: KT, value: VT) -> t.Dict[KT, VT]:
        """Set a new key-value pair with given `key` and `pair` and returns the key-value pair created

        Parameters
        ----------
        key: Any
            The key of the pair
        value: Any
            Value of the pair
        """
        if len(self._cache) >= self.max_size:
            self._cache.popitem(last=False)
            self.current_size -= 1
            self._cache[key] = value
            self._cache.move_to_end(key)
            self.current_size += 1
            return {key: value}
        self._cache[key] = value
        self._cache.move_to_end(key)
        self.current_size += 1
        return {key: value}

    def values(self) -> t.ValuesView[VT]:
        """D.values() -> a set-like object providing a view on D's values"""
        return self._cache.values()
