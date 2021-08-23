# lru-od
Python implementation of LRU-Cache using `OrderedDict`

## Installing
**Python 3.7 or higher required!**

To install the stable version of the library:
```sh
# on linux/macOS
python3 -m pip install lru-od

# windows
py -3 -m pip install lru-od
```

To install the development version of the library:
```sh
$ git clone https://github.com/XiehCanCode/lru-od
$ cd lru-od
$ python3 -m pip install -U .
```

## Example
```py
from lru import LRUCache

cache: LRUCache[str, str] = LRUCache(max_size=2)
cache.set("foo", "bar") # you can also use: cache['foo'] = 'bar'
cache.set("bar", "foo")
print(cache.get("foo")) # this key-pair would be pushed to end
cache.set("ping", "pong") # since we're exceeding the max size, the least used will be removed, in this case it's {'bar': 'foo'}
```

## API
- **class LRUCache**<br>
    LRU Cache implementation

    Parameters
    ----------
    max_size: Optional[`int`]<br>
        Max size of the cache, default's to 120

    Operations
    ----------
    `x == y`<br>
    `x != y`<br>
    `x in y`<br>

    Methods
    -------
    - **cache_info() -> str**<br>
        Information about the cache
    - **get(key: Any) -> Any | None**<br>
        Get a value of the key-value pair with given `key` if exists
    - **items() -> tuple[Any, Any]**<br>
        D.values() -> a set-like object providing a view on D's items
    - **keys() -> KeysView[Any]**<br>
        D.keys() -> a set-like object providing a view on D's keys
    - **remove(key: Any) -> None**<br>
        Remove a key-value pair associated with the `key` parameter if exists
    - **set(key: Any, value: Any) -> dict[Any, Any]**<br>
        Set/Update a new/existing key-value pair with given `key` and `pair` and returns the key-value pair created/updated
    - **values() -> ValuesView[Any]**<br>
        D.values() -> a set-like object providing a view on D's values