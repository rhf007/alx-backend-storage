#!/usr/bin/env python3
""" MongoDB Operations"""
from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides some stats"""
    c = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = c.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for i in methods:
        count = nginx_collection.count_documents({"method": i})
        print(f'\tmethod {i}: {count}')

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')
