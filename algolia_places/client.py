"""Client for Algolia Places API."""
import json

import requests

from .response import AlgoliaPlacesResponse

class AlgoliaPlacesClient:
    """
    Client for Algolia Places API.
    """
    api_url = 'https://places-dsn.algolia.net/1/places/query'
    api_reverse_url = 'https://places-dsn.algolia.net/1/places/reverse'

    def __init__(self, app_id, api_key):
        """
        Initialize the client using Algolia Application Id and API key.

        :param app_id:          Algolia Application Id
        :param api_key:         Algolia API key
        """
        self.app_id = app_id
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'X-Algolia-Application-Id': self.app_id,
            'X-Algolia-API-Key': self.api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        })
        self._defaults = {}

    def defaults(self, **kwargs):
        """
        Set default values for API calls. Use any of the search parameters
        defined here: https://community.algolia.com/places/rest.html#search-parameters
        """
        self._defaults.update(kwargs)

    def search(self, query, **kwargs):
        """
        Search for a place on Algolia Places API.
        """
        body = self._defaults.copy()
        body.update(query=query, **kwargs)
        resp = self.session.post(self.api_url, data=json.dumps(body))

        resp.raise_for_status()
        return AlgoliaPlacesResponse(resp.json())

    def reverse(self, lat, lon):
        """
        Reverse geocode position on Algolia Places API.
        """
        query_vars = self._defaults.copy()
        query_vars.update({
            'aroundLatLng': str(lat) + ',' + str(lon)
        })
        resp = self.session.get(self.api_reverse_url, params=query_vars)
        resp.raise_for_status()
        return AlgoliaPlacesResponse(resp.json())
