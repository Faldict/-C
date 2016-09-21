#!/bin/usr/env python
import requests
import re
from BeautifulSoup import BeautifulSoup


def parseIMG(content):
	imgset = set()
	soup = BeautifulSoup(content)
	for img in soup.findAll('img'):
		imgset.add(str(img.get('src', '')))
	if len(imgset) > 0:
		return imgset
	else :
		return -1


def main():
	headers = {
	'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
	'Accept-Encoding': 'gzip,deflate',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'
}
	r = requests.get("http://www.github.com", headers)
	imgset = parseIMG(r.text)
	if imgset != -1:
		fp = open("res2.txt",'w')
		for u in imgset:
			fp.write(str(u))
		fp.close()
		print "Parse IMGs successfully!"
	else:
		print "No IMG fetched!"

if __name__ == '__main__':
	main()