#!/usr/bin/env python3
'''
NoSQL
'''


from pymongo import MongoClient


def log_stats():
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://localhost:27017/')
    logs_collection = client.logs.nginx

    # Number of documents
    total_docs = logs_collection.count_documents({})
    print(f"{total_docs} logs")

    print("Methods:")
    # Number of documents by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    # Number of documents with method=GET and path=/status
    count = logs_collection.count_documents
    ({'method': 'GET', 'path': '/status'})
    print(f"{count} status check")


if __name__ == "__main__":
    log_stats()
