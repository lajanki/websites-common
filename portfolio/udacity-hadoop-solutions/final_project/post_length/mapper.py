#!/usr/bin/python

"""
Problem
Write a MapReduce program that would process the forum_node data and output the length of the post and the average answer
(just answer, not comment) length for each post.


Input (forum_node.tsv)
id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id	added_at	score	state_string
last_edited_id	last_activity_by_id	last_activity_at	active_revision_id	extra_count	extra_ref_id	extra_count	marked


Filter abs_parent_id and node_type from each row and compute the length of each question.

Outputs
abs_parent_id	node type	len(body)

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
		body = line[4]
		node_type = line[5]
		parent_id = line[6]
		abs_parent_id = line[7]
		added_at = line[8]
		score = line[9]

		# If post is a top level node, set abs_parent_id == id_
		# so that questions will be sorted together with their answers.
		if node_type == "question":
			abs_parent_id = id_

		# Format the line to write to stdout.
		row = [abs_parent_id, node_type, len(body)]
		writer.writerow(row)

