#!/usr/bin/python3
""" takes in a letter and sends a POST request \
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        letter = {'q': ""}
    else:
        letter = {'q': argv[1]}

    r = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        j = r.json()
        if j == {}:
            print("No result")
        else:
            print("[{}] {}".format(j['id'], j['name']))
    except Exception:
        print("Not a valid JSON")
