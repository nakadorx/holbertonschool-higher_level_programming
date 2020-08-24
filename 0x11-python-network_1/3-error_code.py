#!/usr/bin/python3
""" holb """
import urllib.request
import sys


reqq = urllib.request.Request(sys.argv[1])
try:
    with urllib.request.urlopen(reqq) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
