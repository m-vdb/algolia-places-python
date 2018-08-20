import unittest

from algolia_places.hit import AlgoliaPlacesHit
from algolia_places.response import AlgoliaPlacesResponse


class AlgoliaPlacesResponseTestCase(unittest.TestCase):

    def test_init(self):
        data = {
            'hits': [
                {'objectID': 42},
                {'objectID': 43},
            ],
            'nbHits': 2
        }
        resp = AlgoliaPlacesResponse(data)
        self.assertEqual(resp.data, data)
        self.assertEqual(resp.nbHits, 2)
        self.assertEqual(len(resp.hits), 2)
        hit1, hit2 = resp.hits
        self.assertIsInstance(hit1, AlgoliaPlacesHit)
        self.assertEqual(hit1.id, 42)
        self.assertIsInstance(hit2, AlgoliaPlacesHit)
        self.assertEqual(hit2.id, 43)
