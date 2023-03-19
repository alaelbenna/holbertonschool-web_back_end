#!/usr/bin/env python3
"""list all documents module"""

def list_all(mongo_collection):
    """list all documents in a collection"""
    document = mongo_collection.find()

    if not document:
        return []
    return document
