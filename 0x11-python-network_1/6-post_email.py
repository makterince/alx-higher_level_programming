#!/usr/bin/python3
"""
   Send POST request to URL with email parameter
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.post(argv[1], data={"email": argv[2]})
    print(res.text)
