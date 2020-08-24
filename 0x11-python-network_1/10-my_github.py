 
#!/usr/bin/python3
"""
holb
"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    reqq = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    reqq = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        print(reqq.json()['id'])
    except:
        print('None')