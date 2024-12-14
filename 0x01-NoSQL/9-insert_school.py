#!/usr/bin/env python3
"""
Insert a document in Python
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert into a collection
    """
    d = mongo_collection.insert_one(kwargs)
    return d.inserted_id
