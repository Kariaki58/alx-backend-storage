#!/usr/bin/env python3
"""function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """top students"""
    return mongo_collection.aggregate([
        { "$project": { "name": 1, "averageScore": { "$avg": "$topics.score" } } },
        {"$sort": { "averageScore": -1 }}
    ])