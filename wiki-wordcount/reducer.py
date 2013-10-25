#!/usr/bin/env python

from operator import itemgetter
import sys

total = 0

for line in sys.stdin:
    line = line.strip()
    n = int(line)
    total += n

print total
