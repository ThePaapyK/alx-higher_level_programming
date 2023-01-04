#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and \
displays the body of the response (decoded in utf-8)."""
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            content = body.decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
