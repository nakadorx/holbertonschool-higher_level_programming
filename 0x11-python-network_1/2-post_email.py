#!/usr/bin/python3
""" holb"""
import urllib.request
import sys


if __name__ == '__main__':
    data = "email=" + sys.argv[2]
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
