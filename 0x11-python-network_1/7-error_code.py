#!/usr/bin/python3
"""
holb
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    reqq = requests.get(url)
    if reqq.status_code >= 400:
        print("Error code: {}".format(reqq.status_code))
    else:
        print(reqq.text)
