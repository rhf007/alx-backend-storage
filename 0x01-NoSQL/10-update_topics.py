#!/usr/bin/env python3
'''
update
'''


def update_topics(mongo_collection, name, topics):
    '''
    update docs
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
