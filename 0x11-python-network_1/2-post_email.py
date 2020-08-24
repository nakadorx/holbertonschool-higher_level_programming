#!/usr/bin/python3
""" holb"""
import urllib.request
import sys


d = "email=" + sys.argv[2]
d = d.encode('ascii')
reqq = urllib.request.Request(sys.argv[1], d)
with urllib.request.urlopen(reqq) as response:
    html = response.read()
    print(html.decode('utf-8'))
