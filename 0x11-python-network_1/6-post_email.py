#!/usr/bin/python3
"""
holb
"""
import requests
import sys


reqq = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print(reqq.text)
