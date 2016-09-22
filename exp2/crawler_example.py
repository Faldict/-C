#!/usr/bin/env python

def union_bfs(a, b):
	for ele in b:
		if ele not in a:
			a.insert(0, ele)

def crawl(seed, method):
	tocrawl = [seed]
	crawled = []
	graph = {}
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			outlinks = get_all_links(content)
			globals()['union_%s' % method](tocrawl, outlinks)
			if page in g.keys:
				graph[page] = g[page]
			else:
				graph[page] = []
	return graph, crawled

a = [1, 2, 3]
b = [2, 4, 4, 5]

union_bfs(a, b) 
print a, b