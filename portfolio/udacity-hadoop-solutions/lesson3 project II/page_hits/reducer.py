#!/usr/bin/python

"""
Problem:
Write a MapReduce program which will display the number of hits for each different file on the Web site.


Input
request_file

Outputs:
file\thit_count

4.12.2016
"""


import sys

old_file = None
count = 0

for line in sys.stdin:
    data = line.strip().split()
    if len(data) != 3:
        # Something has gone wrong. Skip this line.
        continue

    method, file, request = data

    # Check if file has changed and print its results.
    if old_file and file != old_file:
        print "{0}\t{1}".format(old_file, count)
        count = 0
      

    old_file = file
    count += 1
    

# Print the final file.
if old_file != None:
    print "{0}\t{1}".format(old_file, count)

