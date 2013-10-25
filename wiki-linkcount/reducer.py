#!/usr/bin/env python

from operator import itemgetter
from collections import defaultdict
import sys
import heapq

TOP = 10

counts = defaultdict(lambda: 0)

for line in sys.stdin:
    line = line.strip()
    counts[line] += 1

# print the top N linked pages, with the total number of links
topN = heapq.nlargest(TOP, counts.iteritems(), key=lambda i: i[1])
for k, v in topN:
    print '%s\t%s' % (k, v)
