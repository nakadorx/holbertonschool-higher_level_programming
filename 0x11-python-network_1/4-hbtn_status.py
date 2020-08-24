#!/usr/bin/python3
""" holb """
import requests


reqq = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type:", type(reqq.text))
print("\t- content:", reqq.text)
