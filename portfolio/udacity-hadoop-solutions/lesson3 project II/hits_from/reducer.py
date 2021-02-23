#!/usr/bin/python

"""
Problem:
Write a MapReduce program which determines the number of hits to the site made by each different IP address.


Input
ip_address

Outputs:
ip_address hit_count


4.12.2016
"""


import sys


old_address = None
count = 0

for line in sys.stdin:
    data = line.strip().split()
    if len(data) != 1:
        # Something has gone wrong. Skip this line.
        continue

    address = data[0]

    # Check if file has changed and print its results.
    if old_address and address != old_address:
        print "{0}\t{1}".format(old_address, count)
        count = 0
      

    old_address = address
    count += 1
    

# Print the final address summary.
if old_address != None:
    print "{0}\t{1}".format(old_address, count)

