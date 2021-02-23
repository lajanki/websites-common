#!/usr/bin/python

"""
Problem:
Find the most popular file on the website, ie. the file listed the most number of times in access_log.


Input
file_path

Outputs:
top_file   hit_count


4.12.2016
"""

import sys

old_file = None
most_popular = None
current_max = 0
count = 0

for line in sys.stdin:
    data = line.strip().split()
    if len(data) != 1:
        # Something has gone wrong. Skip this line.
        continue

    file = data[0]

    # Check if file has changed.
    if old_file and file != old_file:
        # Check if old_file is the new top hit.
        if count > current_max:
            current_max = count
            most_popular = old_file

        # Set hit counter back to 0 regardless of whether the previous file was the new top hit or not.
        count = 0
      

    old_file = file
    count += 1
    

# Print the most popular file.
if old_file != None:
    print "{0}\t{1}".format(most_popular, current_max)

