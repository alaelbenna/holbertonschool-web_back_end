#!/usr/bin/env python3
"""find and update a document module"""


def update_topics(mongo_collection, name, topics):
        """find an attribute and change its value"""

        if mongo_collection:
            mongo_collection.update_many({"name": name}, { '$set': { "topics": topics} })
