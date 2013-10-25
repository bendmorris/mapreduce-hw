#!/usr/bin/env python
import sys
import re

# wikipedia links are like [[this]] or [[this|some text]]
wiki_link = re.compile('\[\[([^\]\|]+)(\]\]|\|[^\]]+]])')

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
    
    # find the page name for all page links
    matches = (match[0] for match in wiki_link.findall(line))

    for match in matches:
        # print each link line by line
        print match
