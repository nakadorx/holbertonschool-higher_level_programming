#!/usr/bin/python3
""" holb """
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    reqq = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(reqq) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
