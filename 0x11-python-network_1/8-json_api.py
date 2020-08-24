#!/usr/bin/python3
"""
holb
"""
import requests
import sys

if __name__ == '__main__':
    ll = "" if len(sys.argv) == 1 else sys.argv[1]
    payl = {"q": ll}
    req = requests.post("http://0.0.0.0:5000/search_user", data=payl)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
