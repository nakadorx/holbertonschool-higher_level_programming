#!/usr/bin/python3
"""
holb
"""
import requests
import sys


try:
    qvvq = sys.argv[1]
except:
    qvvq = ""
reqq = requests.post('http://0.0.0.0:5000/search_user', data={'q': qvvq})
try:
    print("[{}] {}".format(reqq.json()['id'], reqq.json()['name']))
except ValueError:
    print("Not a valid JSON")
except:
    print("No result")