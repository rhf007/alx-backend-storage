#!/usr/bin/env python3
"""
Aggregate operations
"""
from pymongo import MongoClient
from collections import OrderedDict
from typing import Tuple


def get_nginx_stats() -> Tuple:
    """
    Queries nginx collection for specific data
    """
    client: MongoClient = MongoClient()
    db = client.logs
    collection = db.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    method_stats = []
    for method in methods:
        method_count = collection.count_documents({'method': method})
        method_stats.append({'method': method, 'count': method_count})
    doc_count = collection.estimated_document_count()
    status_path_stats = collection.count_documents({'method': 'GET',
                                                    'path': '/status'})
    pipeline = [{'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
                {'$sort': OrderedDict([('count', -1)])},
                {'$limit': 10}]
    top_ips = collection.aggregate(pipeline)
    client.close()
    return doc_count, method_stats, status_path_stats, top_ips


def print_nginx_stats() -> None:
    """
    Prints stats from nginx query
    """
    doc_count, method_stats, status_path_stats, top_ips = get_nginx_stats()
    print(f'{doc_count} logs')
    print('Methods:')
    for method in method_stats:
        print(f'\tmethod {method.get("method")}: {method.get("count")}')
    print(f'{status_path_stats} status check')
    print('IPs:')
    for ip in top_ips:
        print(f'\t{ip.get("_id")}: {ip.get("count")}')


if __name__ == '__main__':
    print_nginx_stats()
