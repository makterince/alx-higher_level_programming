#!/usr/bin/python3
""" Send request to URL and retrieve response """
if __name__ == "__main__":
    import requests

    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
