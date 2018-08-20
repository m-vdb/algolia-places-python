"""Base structures."""


class BaseObject:
    """
    Base object class.
    """
    DIRECT_LOOKUPS = []

    def __dir__(self):
        """
        Give nice output to dir() calls.
        """
        return sorted(self.DIRECT_LOOKUPS + super().__dir__())

    def __getattribute__(self, attr):
        """
        All attributes in `DIRECT_LOOKUPS` can be used directly
        on the class instead of using the underlying `hit` dict.
        """
        if attr in self.DIRECT_LOOKUPS:
            return self.hit[attr]

        return super().__getattribute__(attr)
