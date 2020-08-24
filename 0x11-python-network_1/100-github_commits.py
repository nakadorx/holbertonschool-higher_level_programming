#!/usr/bin/python3
"""
holb
"""
import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/repos/' + sys.argv[2] + '/' + sys.argv[1] + \
            '/commits'
    reqq = requests.get(url)
    try:
        for i in range(10):
            print("{}: {}".format(reqq.json()[i]['sha'],
                                    reqq.json()[i]['commit']['author']['name']))
    except:
        pass
