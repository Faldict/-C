#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    alpha, length, count = line.split('\t')
    print "%s\t%s" % (alpha, float(length) / float(count))
