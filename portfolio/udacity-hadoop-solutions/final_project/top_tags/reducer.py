#!/usr/bin/python

"""
Problem
Write a MapReduce program that would output Top 10 tags, ordered by
the number of questions they appear in.

Input
tag	1

Count the occurances of each tag and keep a list of the top 10 tags.

Outputs
tag1	tag2	...	tag10

4.12.2016
"""


import sys
import csv

old_tag = None
SIZE = 10
top_tags = [] # list for (tag, count) -pairs
count = 0


reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)


for line in reader:
	if len(line) != 2:
		continue

	tag = line[0]

	# Tag has changed:
	# check if this tag should be added to top_tags.
	if old_tag and tag != old_tag:

		# check if top_tags currently has < SIZE elements
		# or the current count is > min(top_tags)
		if len(top_tags) < SIZE or count > top_tags[-1][1]:
			new = (old_tag, count)
			top_tags.append(new)

			# Sort by count and remove any extra items.
			top_tags = sorted(top_tags, key = lambda x: x[1], reverse = True)
			top_tags = top_tags[:SIZE]

		count = 0

	count += 1
	old_tag = tag


# Process the final author_id.
if old_tag:
	if len(top_tags) < SIZE or count > top_tags[-1][1]:
		new = (old_tag, count)
		top_tags.append(new)

		# sort and delete the last item
		top_tags = sorted(top_tags, key = lambda x: x[1], reverse = True)
		top_tags = top_tags[:SIZE]


# Write top_tags to stdout
for item in top_tags:
	writer.writerow(item)