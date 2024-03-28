#!/usr/bin/env python3
"""writing strings to Redis"""
import redis
from typing import Union
import uuid


class Cache:
    """cache class"""
    _redis = redis.Redis()
    def __init__(self) -> None:
        """instance method"""
        Cache._redis.flushdb()
    
    
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """redis store"""
        hash = str(uuid.uuid4())
        Cache._redis.set(hash, data)
        return hash