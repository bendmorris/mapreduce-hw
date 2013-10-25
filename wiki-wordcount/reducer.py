#!/usr/bin/env python

from operator import itemgetter
import sys

total = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    n = int(line)
    total += n

print total
