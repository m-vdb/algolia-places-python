# algolia-places-python
API wrapper for Algolia Places API. This module **only supports Python 3**.

[![Build Status](https://travis-ci.org/m-vdb/algolia-places-python.svg?branch=master)](https://travis-ci.org/m-vdb/algolia-places-python)
[![Coverage Status](https://coveralls.io/repos/github/m-vdb/algolia-places-python/badge.svg?branch=master)](https://coveralls.io/github/m-vdb/algolia-places-python?branch=master)
[![Pypi version](https://img.shields.io/pypi/v/algolia-places-python.svg)](https://pypi.python.org/pypi/algolia-places-python)

## Installation

```
$ pip install aloglia-places-python
```


## Usage

```python
from algolia_places import AlgoliaPlacesClient


client = AlgoliaPlacesClient('<your app id>', '<your api key>')

# set defaults for all calls
client.defaults(language='en', countries=['us'], type='city')

# do a search
resp = client.search('San Diego')

# do a search and override defaults
resp = client.search('San Diego', type='address')

# access results
for hit in resp.hits:
  # do something with hit
  pass
```

## How to

Publish on pypi:

```bash
$ python setup.py sdist upload
```
