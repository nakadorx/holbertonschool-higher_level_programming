#!/usr/bin/python3
""" holb """
import requests

if __name__ == '__main__':
	url = 'https://intranet.hbtn.io/status'
	reqq = requests.get(url)
	print("Body response:")
	print("\t- type:", type(reqq.text))
	print("\t- content:", reqq.text)
