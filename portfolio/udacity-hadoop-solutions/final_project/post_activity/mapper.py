#!/usr/bin/python

"""

Problem:
In this exercise your task is to find for each student what is the hour during
which the student has posted the most posts.

Input (forum_node.tsv)
id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id	added_at	score	state_string
last_edited_id	last_activity_by_id	last_activity_at	active_revision_id	extra_count	extra_ref_id	extra_count	marked

Filter author_id and hour part from the timestamp from each row

Output
author_id	hour


4.12.2016
"""


import sys
import csv


# setup a csv reader for reading from stdin and a writer for stdout
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting = csv.QUOTE_ALL)

# skip header row
reader.next()

# output author_id, added_at
for line in reader:

	if len(line) == 19:
		id_ = line[0]
		title = line[1]
		tagnames = line[2]
		author_id = line[3]
		node_type = line[5]
		parent_id = line[6]
		abs_parent_id = line[7]
		added_at = line[8]
		score = line[9]

		# format the line to write to stdout:
		row = [author_id, added_at]
		writer.writerow(row)

