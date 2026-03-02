#!/usr/bin/env python3
"""10-update_topics.py - changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """
    Updates all documents with a given school name, setting the 'topics' field.

    Args:
        mongo_collection: a pymongo collection object
        name (str): the school name to match
        topics (list of str): the list of topics to set

    Returns:
        The result of the update operation (optional)
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result
