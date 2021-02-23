#!/usr/bin/python

"""

Problem:
In this exercise your task is to find for each student what is the hour during
which the student has posted the most posts.

Input
author_id	hour

Use dict to store the number of posts made for each hour.

Output
author_id	most_active_hour

4.12.2016
"""


import sys
import csv
from datetime import datetime


old_id = None

# initialize a dict for number of posts made using hour as key.
# set keys as they are parsed from input
posts = {}


reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)


# loop through user_ids, get the hour of post and store to a dict
for line in reader:
	if len(line) != 2:
		continue

	id_ = line[0]

	# id has changed:
	# write data for previous id 
	if old_id and id_ != old_id:
		# get maximum posts value
		m = max(posts.values())

		# get keys with this value
		keys = [ i for i in posts.keys() if posts[i] == m ]
		for hour in keys:
			writer.writerow([old_id, hour])

		# empty posts
		posts = {}


	# get the hour from input and add to posts
	timestamp = line[1]

	# time is a string in the format of "2012-05-02 15:28:45.479708+00".
	# split by "." and format the beginning to a datetime object
	# to get the hour
	t = timestamp.split(".")[0]
	h = datetime.strptime(t, "%Y-%m-%d %H:%M:%S").hour

	try:
		posts[h] += 1
	# h not yet inserted, add new entry
	except KeyError:
		posts[h] = 1


	old_id = id_
           
            

# print data for the final author_id
if old_id:
	m = max(posts.values())
	keys = [ i for i in posts.keys() if posts[i] == m ]
	for hour in keys:
		writer.writerow([id_, hour])

