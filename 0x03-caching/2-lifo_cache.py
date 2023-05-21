#!/usr/bin/python3
"""Create a Caching System."""


import base_caching


class LIFOCache(base_caching.BaseCaching):
    """A class LIFOCache that inherits from BaseCaching."""

    def __init__(self):
        """Overload init."""
        super().__init__()
        self.CachingKeys = []

    def put(self, key, item):
        """Must assign to the dictionary."""
        if key is None or item is None:
            return
        AmountOfKeys = len(self.CachingKeys)
        if AmountOfKeys == base_caching.BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(str(self.CachingKeys[-1])))
            del self.cache_data[self.CachingKeys[-1]]
            self.CachingKeys = self.CachingKeys[:-1]

        self.CachingKeys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Must return the value."""
        if key is None:
            return None
        return self.cache_data.get(key)
