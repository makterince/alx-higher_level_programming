#!/usr/bin/python3
"""
    script retrieves most recent 10 commits from GitHub repository.
"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Could not retrieve commits.
              HTTP status code {response.status_code}")
        exit()
    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author_name}")
