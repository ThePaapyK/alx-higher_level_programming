#!/usr/bin/python3
""" takes in a letter and sends a POST request \
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        letter = {'q': argv[1]}
    except IndexError:
        letter = {'q': ""}

    r = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    if r.status_code == 204:
        print("No result")
    else:
        try:
            j = r.json()
            print("[{}] {}".format(j['id'], j['name']))
        except requests.exceptions.JSONDecodeError:
            print("Not a valid JSON")
