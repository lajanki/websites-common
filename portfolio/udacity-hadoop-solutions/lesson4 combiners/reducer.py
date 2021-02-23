#!/usr/bin/python

# Problem: Write a MapReduce program that processes the purchases.txt file and outputs
# sum of sales for each weekday. Make sure that the logic that you use in reducer code
# can be used to calculate intermediate value on mappers.

# Loop through weekday and compute the mean

import sys

old_day = None
prices = []


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    weekday, price = data

    if old_day and weekday != old_day:
        print "{0}\t{1}".format(old_day, sum(prices))
        #old_day = weekday
        prices = []

    old_day = weekday
    prices.append(float(price))

if old_day != None:
  	print "{0}\t{1}".format(old_day, sum(prices))
