#!/usr/bin/env python

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        data = line.split()
        page = data[0]
        rank = float(data[1])
        links = data[2:]
        print "%s\t%s\t%s" % (page, rank, '\t'.join(links))
        for link in links:
            print "%s\t%s" % (link, rank/float(len(links)))


if __name__ == '__main__':
    main()
