#!/usr/bin/python

"""
Problem:
Provide a sales breakdown by product category across all of our stores.

Input is lines of the form:
2012-01-18	10:17	Charlotte	Garden	483.03	Amex


Get product category and price from the input.

Outputs:
category	price

4.12.2016
"""

import sys


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{}\t{}".format(item, cost)

