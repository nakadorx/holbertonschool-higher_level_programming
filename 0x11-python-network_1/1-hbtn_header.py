#!/usr/bin/python3
""" holb """
import urllib.request
import sys


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.info()['X-Request-Id'])
