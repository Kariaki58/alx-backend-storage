#!/usr/bin/env python3
"""writing strings to Redis"""
import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    """cache class"""
    def __init__(self) -> None:
        """instance method"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    
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