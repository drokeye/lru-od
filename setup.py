from setuptools import setup
import re

version = ""
with open("lru/__init__.py") as f:
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    if not match:
        raise RuntimeError("version is not set")
    else:
        version = match.group(1)

readme = ""
with open("README.md") as f:
    readme = f.read()

packages = ["lru"]

setup(
    name="lru-od",
    author="XiehCanCode",
    url="https://github.com/XiehCanCode/lru-od",
    version=version,
    packages=packages,
    license="MIT",
    description="Python implementation of LRU Cache",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires=">=3.7.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
