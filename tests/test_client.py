import unittest

from mock import patch
import requests

from algolia_places import AlgoliaPlacesClient
from algolia_places.response import AlgoliaPlacesResponse


class AlgoliaPlacesClientTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.client = AlgoliaPlacesClient(
            'xxx-app-id-xxx',
            'xxx-api-key-xxx'
        )

    def test_init(self):
        self.assertEqual(self.client.app_id, 'xxx-app-id-xxx')
        self.assertEqual(self.client.api_key, 'xxx-api-key-xxx')
        self.assertIsInstance(self.client.session, requests.Session)
        self.assertEqual(self.client.session.headers['X-Algolia-Application-Id'], 'xxx-app-id-xxx')
        self.assertEqual(self.client.session.headers['X-Algolia-API-Key'], 'xxx-api-key-xxx')
        self.assertEqual(self.client.session.headers['Content-Type'], 'application/json')
        self.assertEqual(self.client.session.headers['Accept'], 'application/json')
        self.assertEqual(self.client._defaults, {})

    def test_defaults(self):
        self.client.defaults(language='en', type='city')
        self.assertEqual(self.client._defaults, {
            'language': 'en',
            'type': 'city',
        })

    @patch.object(requests.Session, 'post')
    def test_search(self, session_post):
        session_post.return_value.json.return_value = {
            'hits': [
                {'objectID': 1337},
                {'objectID': 1338},
            ]
        }
        resp = self.client.search('San Fran')
        session_post.assert_called_with(
            self.client.api_url,
            data='{"query": "San Fran"}'
        )
        session_post.return_value.raise_for_status.assert_called_with()
        session_post.return_value.json.assert_called_with()
        self.assertIsInstance(resp, AlgoliaPlacesResponse)
        self.assertEqual(len(resp.hits), 2)

    @patch.object(requests.Session, 'post')
    def test_search_with_defaults(self, session_post):
        session_post.return_value.json.return_value = {
            'hits': [
                {'objectID': 1337},
                {'objectID': 1338},
            ]
        }
        self.client.defaults(language='en')
        resp = self.client.search('San Fran')
        session_post.assert_called_with(
            self.client.api_url,
            data='{"language": "en", "query": "San Fran"}'
        )
        session_post.return_value.raise_for_status.assert_called_with()
        session_post.return_value.json.assert_called_with()
        self.assertIsInstance(resp, AlgoliaPlacesResponse)
        self.assertEqual(len(resp.hits), 2)

    @patch.object(requests.Session, 'post')
    def test_search_override_defaults(self, session_post):
        session_post.return_value.json.return_value = {
            'hits': [
                {'objectID': 1337},
                {'objectID': 1338},
            ]
        }
        self.client.defaults(language='en')
        resp = self.client.search('San Fran', language='fr')
        session_post.assert_called_with(
            self.client.api_url,
            data='{"language": "fr", "query": "San Fran"}'
        )
        session_post.return_value.raise_for_status.assert_called_with()
        session_post.return_value.json.assert_called_with()
        self.assertIsInstance(resp, AlgoliaPlacesResponse)
        self.assertEqual(len(resp.hits), 2)
