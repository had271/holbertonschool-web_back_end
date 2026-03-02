#!/usr/bin/env python3
"""11-schools_by_topic.py - returns schools with a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that include the given topic in their 'topics' field.

    Args:
        mongo_collection: a pymongo collection object
        topic (str): the topic to search for

    Returns:
        List of school documents (dictionaries). Empty list if none found.
    """
    if not mongo_collection:
        return []

    return list(mongo_collection.find({"topics": topic}))
