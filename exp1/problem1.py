import requests
#!/usr/bin/env python
import requests
import re
from BeautifulSoup import BeautifulSoup


def parseURL(content):
	urlset = set()
	soup = BeautifulSoup(content)
	for a in soup.findAll('a'):
		urlset.add(str(a.get('href', '')))
	if len(urlset) > 0:
		return urlset
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
	urlset = parseURL(r.text)
	if urlset != -1:
		fp = open("res1.txt",'w')
		for u in urlset:
			fp.write(str(u))
		fp.close()
		print "Parse URLs successfully!"
	else:
		print "No URL fetched!"

if __name__ == '__main__':
	main()