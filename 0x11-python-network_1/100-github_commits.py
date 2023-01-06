#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the repository"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10&sort\
          =commiter-date&order=desc".format(argv[2], argv[1])
    r = requests.get(url)
    j = r.json()
    for commit in j:
        print("{}: {}".format(commit['sha'],
                              commit['commit']['author']['name']))
