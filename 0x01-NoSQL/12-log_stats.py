#!/usr/bin/env python3
"""import function"""
from pymongo import MongoClient


connect = MongoClient('mongodb://127.0.0.1:27017')
db = connect.logs
mongo_collection_nginx = db.nginx

total_logs = mongo_collection_nginx.count_documents({})

print(f"{total_logs} logs")

http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: mongo_collection_nginx.count_documents({"method": method}) for method in http_methods}

print("Methods:")
for method, count in method_counts.items():
    print(f"\tmethod {method}: {count}")

status_check_count = mongo_collection_nginx.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check_count} status check")
