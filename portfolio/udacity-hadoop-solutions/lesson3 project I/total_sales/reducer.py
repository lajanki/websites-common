#!/usr/bin/python

"""
Problem:
Find the total sales value across all the stores, and the total number of sales.
Assume there is only one reducer.

Input
price

Read the price of each item and keep count of the total price and the number of sales made.

Outputs
category	total_cost	number_of_sales


4.12.2016
"""

import sys

total_price = 0
total_sales = 0


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 1:
        # Something has gone wrong. Skip this line.
        continue

    total_price += float(data[0])
    total_sales += 1


print "{}\t{}".format(total_price, total_sales)

