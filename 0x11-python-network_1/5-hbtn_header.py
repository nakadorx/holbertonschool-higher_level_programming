#!/usr/bin/python3
""" holb
"""
import requests
import sys


try:
    reqq = requests.get(sys.argv[1])
    print(reqq.headers['X-Request-Id'])
except:
    pass
