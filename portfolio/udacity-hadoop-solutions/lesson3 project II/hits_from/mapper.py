#!/usr/bin/python

"""
Problem:
Write a MapReduce program which determines the number of hits to the site made by each different IP address.


Input is lines of the form
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
with items including
* IP address of the client
* identity of the client, or "-" if it's unavailable
* username of the client, or "-" if it's unavailable
* the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
* the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
* the status code
* the size of the object returned to the client. Will be "-" in case of status code 304.

Outputs
ip_address


4.12.2016
"""

import sys

for line in sys.stdin:
	# Split input by space:
	# time gets split to 2 (timestamp, timezone)
	# request line to 3 (http method, file, http version)
    data = line.strip().split()
    if len(data) == 10:
        ipaddr, clientid, uname, time, time_zone, req_method, req_file, req_string, status, size = data
        print "{0}".format(ipaddr)

