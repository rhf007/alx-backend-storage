#!/usr/bin/env python3
"""pymongo """


def list_all(mongo_collection):
    """List all documents """
    docs = mongo_collection.find()

    if docs.count() == 0:
        return []

    return docs
