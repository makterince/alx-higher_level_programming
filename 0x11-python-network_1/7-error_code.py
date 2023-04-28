#!/usr/bin/python3
"""
    Check if HTTP status code is greater than or equal to 400
"""
if __name__ == "__main__":
    import requests
    from requests.exceptions import HTTPError
    from sys import argv

    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
