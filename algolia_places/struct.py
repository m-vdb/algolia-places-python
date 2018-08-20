"""Base structures."""


class BaseObject:
    """
    Base object class.
    """
    DIRECT_LOOKUPS = []

    def __init__(self, data):
        self.data = data

    def __dir__(self):
        """
        Give nice output to dir() calls.
        """
        return sorted(self.DIRECT_LOOKUPS + super().__dir__())

    def __getattribute__(self, attr):
        """
        All attributes in `DIRECT_LOOKUPS` can be used directly
        on the class instead of using the underlying `data` dict.
        """
        if attr == 'DIRECT_LOOKUPS' or attr not in self.DIRECT_LOOKUPS:
            return super().__getattribute__(attr)

        return self.data[attr]
