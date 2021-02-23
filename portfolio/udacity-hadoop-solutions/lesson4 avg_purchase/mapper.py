#!/usr/bin/python

# Problem: Write a MapReduce program that processes the purchases.txt file and outputs
# mean of sales for each weekday

# ouputs (weekday, price) pairs for each line in purchases.txt


import sys
from datetime import datetime


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print "{}\t{}".format(weekday, cost)




