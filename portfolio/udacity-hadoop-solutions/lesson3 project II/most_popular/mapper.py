#!/usr/bin/python

"""
Problem:
Find the most popular file on the website, ie. the file listed the most number of times in access_log.


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

Output: file_path

4.12.2016
"""


import sys

for line in sys.stdin:
	# Get the file from the file path by splitting first by " and then by space.
	data = line.split("\"")
	if len(data) == 3:
		path = data[1].split()[1] # get the filepath from the middle of GET /assets/js/lowpro.js HTTP/1.1
		print "{0}".format(path.replace("http://www.the-associates.co.uk", ""))  # remove domain name from the file path

