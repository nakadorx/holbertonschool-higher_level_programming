#!/usr/bin/python3
""" holb"""
import urllib.request


reqq = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(reqq) as response:
    print("Body response:")
    html = response.read()
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('utf-8'))
