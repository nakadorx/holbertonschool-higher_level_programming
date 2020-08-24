 
#!/usr/bin/python3
"""
holb
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        print(r.json()['id'])
    except:
        print('None')