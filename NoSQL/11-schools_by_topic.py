#!/usr/bin/env python3
"""
NoSQL
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that changes all topics of a school document based on the name
    """
    value = {"topics": topic}
    return mongo_collection.find(value)
