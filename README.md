# algolia-places-python
API wrapper for Algolia Places API. This module **only supports Python 3**.

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
