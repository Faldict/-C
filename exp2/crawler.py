#!/usr/bin/env python

__author__ = "Wang Jialu"
__date__ = "2016-09-22"

from BeautifulSoup import BeautifulSoup
import urllib2
import re 
import urlparse
import os
import urllib
import string

def valid_filename(s):
	valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
	s = ''.join(c for c in s if c in valid_chars)
	return s

def get_page(page):
	content = ''
	try:
		req = urllib2.urlopen(page)
	except:
		pass
	else:
		content = req.read()
	return content

def get_all_links(content, page):
	links = []
	soup = BeautifulSoup(content)
	for a in soup.findAll('a', {'href': re.compile('^http|^/')}):
		url = a.get('href')
		if url[0] == '/':
			url = urlparse.urljoin(page, url)
		links.append(url) 
	return links

def union_dfs(a,b):
	for e in b:
		if e not in a:
			a.append(e)

def union_bfs(a,b):
	for ele in b:
		if ele not in a:
			a.insert(0, ele)


def add_page_to_folder(page, content):
	index_filename = 'index.txt'
	folder = 'html'
	filename = valid_filename(page)
	index = open(index_filename, 'a')
	index.write(page.encode('ascii', 'ignore') + '\t' + filename + '\n')
	index.close()
	if not os.path.exists(folder):
		os.mkdir(folder)
	f = open(os.path.join(folder, filename), 'w')
	f.write(content)
	f.close

def crawl(seed_url, crawler_method, max_page):
	tocrawl = [seed_url]
	crawled = []
	graph = {}
	count = 0

	while(tocrawl):
		page = tocrawl.pop()
		if page not in crawled:
			print page
			content = get_page(page)
			add_page_to_folder(page, content)
			outlinks = get_all_links(content, page)
			globals()['union_%s' % crawler_method](tocrawl, outlinks)
			crawled.append(page)
			graph[page] = outlinks
			count += 1
			if count > max_page:
				break
	return graph, crawled

graph, crawled = crawl('http://www.sjtu.edu.cn', 'dfs', 10)
