#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays \
the value of the variable X-Request-Id in the response \
headertakes in a URL, sends a request to the URL and \
displays the value of the variable X-Request-Id in the response header
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    try:
        print(r.headers['X-Request-Id'])
    except Exception as e:
        print("None")
