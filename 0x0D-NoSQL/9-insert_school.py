#!/usr/bin/env python3
"""insert new document module"""


def insert_school(mongo_collection, **kwargs):
     """insert new document in a collection"""
        result = mongo_collection.insert_one(kwargs)
            return result.inserted_id
