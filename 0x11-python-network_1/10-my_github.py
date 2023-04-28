#!/usr/bin/python3
"""
    script takes users Github details - username and password
    and uses github api to show the user
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    
    headers = {
            "Authorization": "Bearer {}".format(argv[2]),
            "X-GitHub-Api-Version": "2022-11-28"
            }
    res = requests.get("https://api.github.com/user", headers=headers)
    try:
        print(res.json()["id"])
    except KeyError:
        print(None)
