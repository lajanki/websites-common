#!/usr/bin/python

"""
Problem
Write a MapReduce program that for each forum thread (that is a question node with all
it's answers and comments) gives a list of students that have posted there
- either asked the question, answered a question or added a comment.
If a student posted to that thread several times, they should be added to that list
several times as well, to indicate intensity of communication.

Input (forum_node.tsv)
id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id	added_at	score	state_string
last_edited_id	last_activity_by_id	last_activity_at	active_revision_id	extra_count	extra_ref_id	extra_count	marked

Filter abs_parent_id and author_id from each row.

Outputs
abs_parent_id	author_id

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

		# Set top level abs_parent_id to post id.
		if node_type == "question":
			abs_parent_id = id_
			
		writer.writerow((abs_parent_id, author_id))


	