#!/usr/bin/python

"""
Problem:
Find the total sales value across all the stores, and the total number of sales.
Assume there is only one reducer.


Input
date	time	store name	item	description	cost	payment_method

Filter cost from each input row.

Outputs
cost

4.12.2016
"""


import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) < 6:
    	continue

    date, time, store, item, cost, payment = data
    print cost

