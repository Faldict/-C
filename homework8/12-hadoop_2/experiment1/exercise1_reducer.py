#!/usr/bin/env python

from operator import itemgetter
import sys

current_alpha = None
current_count = 0
current_length = 0
alpha = None

for line in sys.stdin:
    line = line.strip()
    alpha, length, count = line.split('\t')

    try:
        count = int(count)
        length = int(length)
    except ValueError:
        continue

    if current_alpha == alpha:
        current_count += count
        current_length += length
    else:
        if current_alpha:
            print "%s\t%s\t%s" % (current_alpha, current_length, current_count)
        current_count = count
        current_length = length
        current_alpha = alpha

if current_alpha == alpha:
    print "%s\t%s\t%s" % (current_alpha, current_length, current_count)
