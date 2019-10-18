import sys
import os
from re import findall
import requests

URL = "https://c9x.me/x86/"

def reload(out):
    global URL
    try:
        site = requests.get(URL)
    except:
        print("can't download instructions data")

    data = findall('<a href="(.*)">(.*)</a>', site.text)
    out = open(out, 'w')

    for link, name in data:
        print(name, URL + link, file=out)

    out.close()

