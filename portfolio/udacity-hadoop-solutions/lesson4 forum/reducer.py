#!/usr/bin/python

"""
Problem
Your goal for this task is to write mapper and reducer code 
that will combine some of the forum and user data. 
In relational algebra, this is known as a join operation. 
At the moment, this is not an auto-gradable exercise, but instructions below are given on how to test your code on your machine. 

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
"""

import sys
import csv

old_id = None


# Init a list for post data to output and a user dict for user related data
# within a post.
posts = []
user = {}

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

# Input is in the format of
# post
# post
# ...
# user 1
#
# post
# user 2

for line in reader:

    data = line
    id_ = data[0]

    # Loop through lines starting with id_ storing post and
    # user data and print when id_ changes.
    if not old_id or id_ == old_id:
        try:
            # See if line is a post or a user.
            if data[1] == "post":
                # Create a new post data entry.
                post_data = {
                    "title": data[3],
                    "tagnames": data[4],
                    "author_id": data[0],
                    "node_type": data[5],
                    "parent_id": data[6],
                    "abs_parent_id": data[7],
                    "added_at": data[8],
                    "score": data[9],
                }
                posts.append(post_data)


            else:
                user["reputation"] = data[2]
                user["gold"] = data[3]
                user["silver"] = data[4]
                user["bronze"] = data[5]

        except IndexError as e:
            print e
            continue


    # id has changed: format and print previous data.
    elif id_ != old_id:
        for post in posts:
            row = [
                id_,
                post["title"],
                post["tagnames"],
                post["author_id"],
                post["node_type"],
                post["parent_id"],
                post["abs_parent_id"],
                post["added_at"],
                post["score"],
                user["reputation"],
                user["gold"],
                user["silver"],
                user["bronze"]
            ]
            writer.writerow(row)

        posts = []

    old_id = id_
           
            


# Process final post.
if old_id:
    for post in posts:
        row = [
            id_,
            post["title"],
            post["tagnames"],
            post["author_id"],
            post["node_type"],
            post["parent_id"],
            post["abs_parent_id"],
            post["added_at"],
            post["score"],
            user["reputation"],
            user["gold"],
            user["silver"],
            user["bronze"]
        ]
        writer.writerow(row)