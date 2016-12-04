#-*- coding: utf-8 -*-
from watson_developer_cloud import DocumentConversionV1
from bs4 import BeautifulSoup
import urllib.request
import json, os

"""
# 지진 pdf 추출
document_conversion = DocumentConversionV1(
	username='f91d53d6-4859-4e19-a67c-03273af66712',
	password='WJPUFzhdTUeq',
	version='2015-12-15'
)

config = {
	'conversion_target': 'NORMALIZED_TEXT'
}

with open(('earthquake.pdf'), 'rb') as document:
	response = document_conversion.convert_document(document=document, config=config)

with open('earthquake.txt', 'w') as output:
	output.write(response.content.decode())
"""

#soup = BeautifulSoup(page, 'html.parser')

"""
# 화산 html 추출
url = 'https://en.wikipedia.org/wiki/Volcano'
headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36'
}
req = urllib.request.Request(url, headers=headers)
page = urllib.request.urlopen(req).read()
with open('volcano.html', 'wb') as document:
	document.write(page)

document_conversion = DocumentConversionV1(
	username='f91d53d6-4859-4e19-a67c-03273af66712',
	password='WJPUFzhdTUeq',
	version='2015-12-15'
)

config = {
	'conversion_target': 'NORMALIZED_TEXT'
}

with open('volcano.html', 'rb') as document:
	response = document_conversion.convert_document(document=document, config=config)

with open('volcano.txt', 'w') as output:
	output.write(response.content.decode())
"""