#!/usr/bin/python3
"""
holb
"""
import requests
import sys


reqq = requests.get(sys.argv[1])
if reqq.status_code >= 400:
    print("Error code:", reqq.status_code)
else:
    print(reqq.text)
