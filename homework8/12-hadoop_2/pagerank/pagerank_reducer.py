#!/usr/bin/env python

import sys

current_page = None
current_rank = 0.0
alpha = 0.85
links = []
num = 4

for line in sys.stdin:
    line = line.strip()
    data = line.split('\t')
    page = data[0]
    rank = data[1]
    if len(data) > 2:
        links = data[2:]
    try:
        rank = float(rank)
    except ValueError:
        continue

    if current_page == page:
        current_rank += rank
    else:
        if current_page:
            current_rank = alpha * current_rank + (1 - alpha) * (1.0 / num)
            links = '\t'.join(links)
            print '%s\t%s\t%s' % (current_page, current_rank, links)
            links = []
        current_rank = rank
        current_page = page

if current_page == page:
    links = '\t'.join(links)
    print "%s\t%s\t%s" % (current_page, current_rank, links)
