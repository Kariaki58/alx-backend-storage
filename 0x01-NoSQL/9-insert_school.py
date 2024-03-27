#!/usr/bin/env python3
"""function that inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """insert a document in python"""
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id