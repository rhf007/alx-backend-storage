#!/usr/bin/env python3
"""
matching data in list
"""


def schools_by_topic(mongo_collection, topic):
    """
    Finds specific topic
    """
    return mongo_collection.find({'topics': topic})
