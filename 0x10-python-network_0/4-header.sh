#!/bin/bash
#  takes in a URL as an argument, sends a GET request to the URL
curl -s $1 -X GET -H "X-HolbertonSchool-User-Id: 98"
