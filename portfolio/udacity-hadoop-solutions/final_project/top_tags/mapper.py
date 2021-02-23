#!/usr/bin/python

"""
Problem
Write a MapReduce program that would output Top 10 tags, ordered by
the number of questions they appear in.

Input (forum_node.tsv)
id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id	added_at	score	state_string
last_edited_id	last_activity_by_id	last_activity_at	active_revision_id	extra_count	extra_ref_id	extra_count	marked


Filter tags from each input line.

Outputs
tag	1

4.12.2016
"""

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting = csv.QUOTE_ALL)

# Skip header row.
reader.next()

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

		if node_type == "question":
			# split tags by spaces
			tags = tagnames.split()
			for tag in tags:
				writer.writerow([tag, 1])


	