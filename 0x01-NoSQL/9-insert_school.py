#!/usr/bin/env python3
''' inserts a new document in a collection based on kwargs.
'''


def insert_school(mongo_collection, **kwargs):
    '''code to inserts a new document in a collection.
    '''
    end_result = mongo_collection.insert_one(kwargs)
    return end_result.inserted_id
