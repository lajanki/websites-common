#!/usr/bin/python

# Problem: Write a MapReduce program that processes the purchases.txt file and outputs
# mean of sales for each weekday

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
     	mean = sum(prices) / len(prices)

        print "{0}\t{1}".format(old_day, mean)
        #old_day = weekday
        prices = []

    old_day = weekday
    prices.append(float(price))

if old_day != None:
	mean = sum(prices) / len(prices)
  	print "{0}\t{1}".format(old_day, mean)
