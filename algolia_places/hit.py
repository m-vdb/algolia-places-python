"""Hit from Algolia Places API."""
from .struct import BaseObject


class AlgoliaPlacesHit(BaseObject):
    """
    Hit from Algolia Places API.
    """
    DIRECT_LOOKUPS = [
        '_highlightResult'
        'admin_level',
        'administrative',
        'country',
        'country_code',
        'county',
        'importance',
        'is_city',
        'is_country',
        'is_highway',
        'is_popular',
        'locale_names',
        'objectID',
        'population',
        'postcode',
    ]

    def __init__(self, hit):
        self.hit = hit

    @property
    def id(self):  # pylint: disable=invalid-name
        """
        Shortcut for id property.
        """
        return self.hit['objectID']

    @property
    def geoloc(self):
        """
        Allow access to `geoloc` property without the starting underscore,
        underscores denote private properties in Python.
        """
        return self.hit['_geoloc']

    @property
    def tags(self):
        """
        Allow access to `tags` property without the starting underscore,
        underscores denote private properties in Python.
        """
        return self.hit['_tags']
