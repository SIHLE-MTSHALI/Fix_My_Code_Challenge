#!/usr/bin/python3
"""
Test file
"""
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/api/v1/status"
    r = requests.get(url)
    print(r.json())
