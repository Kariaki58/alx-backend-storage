#!/usr/bin/env python3
""" list all documents in python """


def list_all(mongo_collection):
    """list all documents"""
    return list(mongo_collection.find())
