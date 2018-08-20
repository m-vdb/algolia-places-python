import unittest

from algolia_places.hit import AlgoliaPlacesHit


class AlgoliaPlacesHitTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.hit = AlgoliaPlacesHit({
            'objectID': 287531,
            '_geoloc': {
                'lat': 92.12,
                'lng': 121.1,
            },
            '_tags': ['city', 'locality'],
        })

    def test_id(self):
        self.assertEqual(self.hit.id, 287531)
        self.assertEqual(self.hit.objectID, 287531)

    def test_geoloc(self):
        self.assertEqual(self.hit.geoloc, {
            'lat': 92.12,
            'lng': 121.1,
        })

    def test_tags(self):
        self.assertEqual(self.hit.tags, ['city', 'locality'])
