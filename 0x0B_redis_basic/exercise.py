#!/usr/bin/env python3

''' redis module
'''

import uuid
import redis


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str) -> str:
        key = str(uuid.uuid4())
            self._redis.set(key, data)
                return key
