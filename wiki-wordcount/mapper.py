#!/usr/bin/env python
import sys

start_tag = '<text xml:space="preserve">'
end_tag = '</text>'

for line in sys.stdin:
    line = line.strip()
    if not line: continue

    if line.startswith(start_tag):
        if line.endswith(end_tag): continue
        line = line[len(start_tag):]
    elif line.startswith('<'):
        continue

    print len(line.split())
