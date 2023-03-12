#!/usr/bin/env python3
"""Module Cache class
"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
        """Decorator that increments the count for that key every time the
            method is called and returns the value returned by the original method.
                """
                    key = method.__qualname__

                        @wraps(method)
                            def wrapper(self, *args, **kwargs):
                                        """Wrapped function
                                                """
                                                        self._redis.incr(key)
                                                                return method(self, *args, **kwargs)
                                                                return wrapper


                                                            def call_history(method: Callable) -> Callable:
                                                                    """Decorator to store the history of inputs and outputs for a particular
                                                                        function.
                                                                            """

                                                                                @wraps(method)
                                                                                    def wrapper(self, *args, **kwargs):
                                                                                                """Wrapped function
                                                                                                        """
                                                                                                                input = str(args)
                                                                                                                        output = str(method(self, *args, **kwargs))
                                                                                                                                self._redis.rpush(method.__qualname__ + ":inputs", input)
                                                                                                                                        self._redis.rpush(method.__qualname__ + ":outputs", output)
                                                                                                                                                return output
                                                                                                                                                return wrapper


                                                                                                                                            def replay(method: Callable):
                                                                                                                                                    """Function that displays the history of calls of a particular function
                                                                                                                                                        """
                                                                                                                                                            key = method.__qualname__
                                                                                                                                                                inputs = key + ":inputs"
                                                                                                                                                                    outputs = key + ":outputs"
                                                                                                                                                                        redis = method.__self__._redis
                                                                                                                                                                            count = redis.get(key).decode("utf-8")
                                                                                                                                                                                print("{} was called {} times:".format(key, count))

                                                                                                                                                                                    in_list = redis.lrange(inputs, 0, -1)
                                                                                                                                                                                        out_list = redis.lrange(outputs, 0, -1)
                                                                                                                                                                                            redis_zipped = list(zip(in_list, out_list))

                                                                                                                                                                                                for a, b in redis_zipped:
                                                                                                                                                                                                            attr, data = a.decode("utf-8"), b.decode("utf-8")
                                                                                                                                                                                                                    print("{}(*{}) -> {}".format(key, attr, data))


                                                                                                                                                                                                                    class Cache:
                                                                                                                                                                                                                            """Cache class
                                                                                                                                                                                                                                """
                                                                                                                                                                                                                                    def __init__(self):
                                                                                                                                                                                                                                                """Constructor method
                                                                                                                                                                                                                                                        """
                                                                                                                                                                                                                                                                self._redis = redis.Redis()
                                                                                                                                                                                                                                                                        self._redis.flushdb()

                                                                                                                                                                                                                                                                            @count_calls
                                                                                                                                                                                                                                                                                @call_history
                                                                                                                                                                                                                                                                                    def store(self, data: Union[str, bytes, int, float]) -> str:
                                                                                                                                                                                                                                                                                                """Method that generates a random key, stores the input data in Redis
                                                                                                                                                                                                                                                                                                        using the random key and return the key.
                                                                                                                                                                                                                                                                                                                """
                                                                                                                                                                                                                                                                                                                        key = str(uuid4())
                                                                                                                                                                                                                                                                                                                                self._redis.set(key, data)
                                                                                                                                                                                                                                                                                                                                        return key

                                                                                                                                                                                                                                                                                                                                        def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
                                                                                                                                                                                                                                                                                                                                                    """Convert the data back to the desired format
                                                                                                                                                                                                                                                                                                                                                            """
                                                                                                                                                                                                                                                                                                                                                                    data = self._redis.get(key)
                                                                                                                                                                                                                                                                                                                                                                            if fn:
                                                                                                                                                                                                                                                                                                                                                                                            return fn(data)
                                                                                                                                                                                                                                                                                                                                                                                                return data

                                                                                                                                                                                                                                                                                                                                                                                                def get_str(self, key: str) -> str:
                                                                                                                                                                                                                                                                                                                                                                                                            """Method that automatically parametrize Cache.get to string
                                                                                                                                                                                                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                                                                                                                                                                                                            data = self._redis.get(key)
                                                                                                                                                                                                                                                                                                                                                                                                                                    return str(data.decode("utf-8"))

                                                                                                                                                                                                                                                                                                                                                                                                                                    def get_int(self, key: str) -> int:
                                                                                                                                                                                                                                                                                                                                                                                                                                                """Method that automatically parametrize Cache.get to int
                                                                                                                                                                                                                                                                                                                                                                                                                                                        """
                                                                                                                                                                                                                                                                                                                                                                                                                                                                data = self._redis.get(key)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        return int(data.decode("utf-8"))
