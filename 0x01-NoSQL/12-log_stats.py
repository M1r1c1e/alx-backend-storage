#!/usr/bin/env python3

"""
A function that shows stats about Nginx request logs stored
in MongoDB.
"""

from pymongo import MongoClient


def Nginx_request():
    """
    Display statistics of different HTTP methods in the nginx logs.

    This function connects to a MongoDB database, retrieves the nginx logs (GET, POST, PUT,
    PATCH, DELETE)
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
    Nginx_request()
