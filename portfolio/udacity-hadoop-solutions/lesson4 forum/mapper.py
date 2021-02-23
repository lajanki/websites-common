#!/usr/bin/python

"""
Problem
Your goal for this task is to write mapper and reducer code 
that will combine some of the forum and user data. 

The goal is to have the output from the reducer with the following fields for each forum post: 
"id"  "title"  "tagnames"  "author_id"  "node_type"  "parent_id"  "abs_parent_id"  "added_at" 
"score"  "reputation"  "gold"  "silver"  "bronze"
 
Note that for each post we have taken some of the information describing the post, 
and joined it with user information. The body of the post is not included in the final output. 
The reason is that it is difficult to handle a multiline body, as it might be split on separate 
lines during the intermediate steps Hadoop performs - shuffle and sort.   

Your mapper code should take in records from both forum_node and forum_users. 
It needs to keep, for each record, those fields that are needed for the final output given above. 
In addition, mapper needs to add some text (e.g. "A" and "B") to mark where each output comes from 
(user information vs forum post information). Example output from mapper is:

"12345"  "A"  "11"  "3"  "4"  "1"
"12345"  "B"   "6336" "Unit 1: Same Value Q"  "cs101 value same"  "question"  "\N"  "\N"  "2012-02-25 08:09:06.787181+00"  "1" 
  
The first line originally comes from the forum_users input. It is from a student with user id: 12345 - the mapper key. 
The next field is the marker A specifying that the record comes from forum_users. 
What follows is the remaining information user information. 

The second line originally comes from the forum_node input. 
It also starts with the student id (mapper key) followed by a marker B and the information about the forum post.  
   
The mapper key for both types of records is the student ID: 
"user_ptr_id" from "forum_users" or  "author_id" from "forum_nodes" file. 
Remember that during the sort and shuffle phases records will be grouped based on the student ID (12345 in our example). 
You can use that to process and join the records appropriately in the reduce phase. 

4.12.2016
"""

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

# Skip header row.
reader.next()

for line in reader:

	# Check if this line is from forum_node.tsv or forum_users.tsv
	# based on number of columns

	# forum_node.tsv: filter the required values from the line and add a "post"
	# keyword to signify forum post.
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

		# Format the line to write to stdout:
		row = [line[3], "post"] # author id as key and "post" to signify forum post
		row.extend([ line[i] for i in (0,1,2,5,6,7,8,9) ]) # extend the rest from the line read

		# Write the output.
		writer.writerow(row)


	# forum_users.tsv: filter poster's data and add a "user" keyword.
	# Use user id as key to match input from forum_node.tsv.
	else:
		row = [line[0], "user"]
		row.extend( line[1:] )
		writer.writerow(row)
