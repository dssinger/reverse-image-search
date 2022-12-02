#!/usr/bin/env python3
import requests
import webbrowser
import sys
import os
import re
from pprint import pprint

filePath = os.path.expanduser('~/Desktop/searchme.jpg')
try:
    if sys.argv[1]:
        filePath = sys.argv[1]
except IndexError:
    pass

searchUrl = 'https://lens.google.com/upload?hl=en&re=df&st=1669959570733&ep=gisbubb'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
m = re.match(r'.*URL=(.*)"', response.text)
fetchUrl = m.group(1)
webbrowser.open(fetchUrl)
