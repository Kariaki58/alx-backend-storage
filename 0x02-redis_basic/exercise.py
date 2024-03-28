#!/usr/bin/env python3
"""writing strings to Redis"""
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """increment function"""
    @wraps(method)
    def count_wraper(self, *args, **kwargs):
        """"""
        class_method = method.__qualname__
        self._redis.incr(class_method)
        return method(self, *args, **kwargs)
    return count_wraper


def call_history(method: Callable) -> Callable:
    """call history"""
    @wraps(method)
    def wrapper(self, *args):
        """wrapper"""
        input_data = method.__qualname__ + ":inputs"
        output_data = method.__qualname__ + ":outputs"
        self._redis.rpush(input_data, str(args))
        result = method(self, *args)
        self._redis.rpush(output_data, str(result))
        return result
    return wrapper
    


class Cache:
    """cache class"""
    def __init__(self) -> None:
        """instance method"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @call_history
    @count_calls
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """redis store"""
        hash = str(uuid.uuid4())
        self._redis.set(hash, data)
        return hash
    
    def get(
        self, key: str, fn: Optional[Callable] = None
        ) -> Union[str, bytes, int, float]:
        """get key"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        """return get string"""
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """return get int"""
        return self.get(key, fn=int)
