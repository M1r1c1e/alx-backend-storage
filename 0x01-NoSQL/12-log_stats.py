#!/usr/bin/env python3

"""
this is a function that displays stats about Nginx request logs stored
in MongoDB.
"""

from pymongo import MongoClient


def  nginx_logs():
    """
    Prints statistics about Nginx request logs
    """

    client = MongoClient()
    nginx = client.logs.nginx

    print(nginx.count_documents({}), "logs")
    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(
            f"\tmethod {method}: {nginx.count_documents({'method': method})}"
        )

    print(f"{nginx.count_documents({'path': '/status'})} status check")


if __name__ == "__main__":
    nginx_logs()
