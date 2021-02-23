#!/usr/bin/python

"""
Problem
Write a MapReduce program that for each forum thread (that is a question node with all
it's answers and comments) gives a list of students that have posted there
- either asked the question, answered a question or added a comment.
If a student posted to that thread several times, they should be added to that list
several times as well, to indicate intensity of communication.

Input
abs_parent_id	author_id

For each post id collect the poster ids to a list.

Outputs
abs_parent_id	list_of_posters


4.12.2016
"""


import sys
import csv

old_id = None
posters = []


reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)

writer.writerow(("Thread ID", "posters"))

for line in reader:
	if len(line) != 2:
		continue

	id_ = line[0]

	# id has changed:
	# write thread_id and list of poster ids.
	if old_id and id_ != old_id:
		writer.writerow((old_id, posters))
		posters = []



	posters.append(line[1])
	old_id = id_

      
            

# Print data for the final thread id.
if old_id:
	writer.writerow((old_id, posters))



