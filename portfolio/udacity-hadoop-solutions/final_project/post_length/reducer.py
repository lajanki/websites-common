#!/usr/bin/python

"""
Problem
Write a MapReduce program that would process the forum_node data and output the length of the post and the average answer
(just answer, not comment) length for each post.


Input
abs_parent_id	node type	len(body)

For each abs_parent_id record response lengths.

Outputs
post_id 	post_length 	avg_response_length

4.12.2016
"""


import sys
import csv
from datetime import datetime

old_id = None

# Initialize fields for answer lengths and top level question length.
ans_lengths = []
post_length = 0


reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)


# Loop through post_ids, see if it is a question or an answer
# and process post length data accordingly.
for line in reader:
	if len(line) != 3:
		continue

	id_ = line[0]

	# New post_id: write current data to stdout.
	if old_id and id_ != old_id:
		if not ans_lengths: # set avg = 0 for cleaner output
			avg = 0
		else:
			avg = sum(ans_lengths) / len(ans_lengths)
		writer.writerow([old_id, post_length, avg])

		ans_lengths = []


	# Check if current line is a question or an answer.
	if line[1] == "question":
		post_length = line[2]

	elif line[1] == "answer":
		ans_lengths.append(float(line[2]))


	old_id = id_


            

# Print data for the final id.
if old_id:
	if not ans_lengths:
		avg = 0
	else:
		avg = sum(ans_lengths) / len(ans_lengths)
	writer.writerow([old_id, post_length, avg])

