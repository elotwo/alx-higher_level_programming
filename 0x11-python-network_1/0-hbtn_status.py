#!/usr/bin/python3
"""
this script is about fetching url from server
"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print('body response:')
    print('-type:', type(html))
    print('-content:', html)
    print('-utf8 content:', html.decode('utf-8'))
