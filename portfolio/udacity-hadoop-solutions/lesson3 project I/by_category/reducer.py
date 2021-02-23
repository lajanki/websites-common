#!/usr/bin/python

"""
Problem:
Provide a sales breakdown by product category across all of our stores.

Input
category   price

Outputs
category   total_cost  number_of_sales

Loop until the category changes and output total sale amount and number of sales made.

4.12.2016
"""

import sys


old_category = None
total_price = 0


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    current_category, current_price = data

    # Check if category has changed and print results.
    if old_category and current_category != old_category:
        print "{}\t{}\t{}".format(old_category, total_price)
        total_price = 0


    total_price += float(current_price)
    old_category = current_category
    

# Print the final store summary.
if old_category != None:
    print "{}\t{}\t{}".format(old_category, total_price)

