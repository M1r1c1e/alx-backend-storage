#!/usr/bin/env python3
"""A module containing a function that list all document"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    doc_list = mongo_collection.find()
    return doc_list
