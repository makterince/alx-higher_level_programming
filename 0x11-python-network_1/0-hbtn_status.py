#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    body = html.decode('utf-8')
    body_lines = body.splitlines()
    for line in body_lines:
        print(f"\t- {line}")
