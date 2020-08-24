#!/usr/bin/python3
""" holb
"""
import requests
import sys


if __name__ == '__main__':
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass
