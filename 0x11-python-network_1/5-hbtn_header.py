#!/usr/bin/python3
"""
    Get value of X-Request-Id header from response
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get(argv[1])
    try:
        print(res.headers["X-Request-Id"])
    except KeyError:
        pass
