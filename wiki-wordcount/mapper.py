#!/usr/bin/env python
import sys

start_tag = '<text xml:space="preserve">'
end_tag = '</text>'

for line in sys.stdin:
    line = line.strip()
    if not line: continue

    if line.startswith(start_tag):
        if line.endswith(end_tag):
            # no text in this article; ignore
            continue

        # strip off the beginning <text> tag
        line = line[len(start_tag):]

    elif line.startswith('<'):
        # this line contains metadata; ignore
        continue

    # print the number of words in this line
    print len(line.split())
