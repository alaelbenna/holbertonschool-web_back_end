#!/usr/bin/python3
"""Create a Caching System."""


import base_caching


class BasicCache(base_caching.BaseCaching):
    """A class BasicCache that inherits from BaseCaching."""

    def put(self, key, item):
        """Must assign to the dictionary."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Must return the value."""
        if key is None:
            return None
        return self.cache_data.get(key)
