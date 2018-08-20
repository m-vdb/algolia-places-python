"""Response from Algolia Places API."""
from .hit import AlgoliaPlacesHit
from .struct import BaseObject


class AlgoliaPlacesResponse(BaseObject):  # pylint: disable=too-few-public-methods
    """
    Response from Algolia Places API.
    """
    DIRECT_LOOKUPS = [
        'degradedQuery',
        'hits',
        'nbHits',
        'params',
        'processingTimeMS',
        'query',
    ]

    def __init__(self, api_response):
        self.api_response = api_response
        self.hits = [AlgoliaPlacesHit(hit) for hit in api_response['hits']]
