#!/bin/bash
# makes a request that causes the server to respond with a message
curl -s $1 -X GET -H "Message: You got me!"
