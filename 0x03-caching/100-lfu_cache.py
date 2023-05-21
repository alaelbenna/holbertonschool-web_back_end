#!/usr/bin/python3
"""Create a Caching System."""


import base_caching


class LFUCache(base_caching.BaseCaching):
    """A class LFUCache that inherits from BaseCaching."""

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
        if key in self.CachingKeys:
            self.CachingKeys.remove(key)
        self.CachingKeys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Must return the value."""
        if key is not None and key in self.CachingKeys:
            self.CachingKeys.remove(key)
            self.CachingKeys.append(key)
            return self.cache_data.get(key)
        return None
