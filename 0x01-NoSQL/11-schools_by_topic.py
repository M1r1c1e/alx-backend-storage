#!/usr/bin/env python3
"""function that list all school with a specific topic`"""


def schools_by_topic(mongo_collection, topic):
    """code that returns the list of school having a specific topic"""
    school_lists = mongo_collection.find(
        {"topics": topic}
    )
    return school_lists
