#!/usr/bin/python3
""" holb """
import urllib.request
import sys


url = sys.argv[1]
reqq = urllib.request.Request(url)
with urllib.request.urlopen(reqq) as response:
    print(dict(response.headers).get("X-Request-Id"))
