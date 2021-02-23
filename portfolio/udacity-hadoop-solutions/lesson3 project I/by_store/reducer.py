#!/usr/bin/python

"""
Problem:
Find the monetary value for the highest individual sale for each separate store.

Input
store  cost

Loop until the store changes and keep track of the highest item seen so far.

Outputs
store   highest_sale

4.12.2016
"""

import sys

old_store = None
current_max = 0


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    current_store, current_price = data

    # Check if store has changed and print results.
    if old_store and current_store != old_store:
        print "{}\t{}".format(old_store, current_max)
        current_max = 0

    if float(current_price) > current_max:
        current_max = float(current_price)

    old_store = current_store
    

# Print the final store summary.
if old_store != None:
    print "{}\t{}".format(old_store, current_max)

