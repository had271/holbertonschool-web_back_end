#!/usr/bin/env python3
"""8-all.py - lists all documents in a collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: a pymongo collection object

    Returns:
        List of documents (dictionaries). Empty list if none found.
    """
    if not mongo_collection:
        return []

    return list(mongo_collection.find())
