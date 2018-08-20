"""Response from Algolia Places API."""
from .hit import AlgoliaPlacesHit
from .struct import BaseObject


class AlgoliaPlacesResponse(BaseObject):  # pylint: disable=too-few-public-methods
    """
    Response from Algolia Places API.
    """
    DIRECT_LOOKUPS = [
        'degradedQuery',
        'nbHits',
        'params',
        'processingTimeMS',
        'query',
    ]

    def __init__(self, data):
        super().__init__(data)
        self.hits = [AlgoliaPlacesHit(hit) for hit in self.data['hits']]
