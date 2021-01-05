#!/usr/bin/env python3
import requests
import webbrowser
import sys
import os

filePath = os.path.expanduser('~/Desktop/searchme.jpg')
try:
    if sys.argv[1]:
        filePath = sys.argv[1]
except IndexError:
    pass

searchUrl = 'http://www.google.com/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
webbrowser.open(fetchUrl)
