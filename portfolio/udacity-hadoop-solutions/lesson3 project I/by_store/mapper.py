#!/usr/bin/python

"""
Problem:
Find the monetary value for the highest individual sale for each separate store.

Input is lines of the form:
2012-01-18	10:17	Charlotte	Garden	483.03	Amex


Print store and cost to stdout.

Outputs:
store	cost

4.12.2016
"""


import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{}\t{}".format(store, cost)

