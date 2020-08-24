#!/usr/bin/python3
""" holb """
import urllib.request
import sys


req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    print(response.info()['X-Request-Id'])
