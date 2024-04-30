#!/usr/bin/env python3
'''
Module to print status of logs and
most Methods
'''
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    nginx_collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f"{nginx_collection.count_documents({})} logs")

    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{count} status check")
