#!/usr/bin/python3
"""
    Check if response body is properly JSON formatted and not empty
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    try:
        q = argv[1]
    except IndexError:
        q = ""

    res = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        res_json = res.json()
        valid = True
    except ValueError:
        valid = False
        print("Not a valid JSON")
        
    if valid:
        if not res_json:
            print("No result")
        else:
            print("[{}] {}".format(res_json["id"], res_json["name"]))
