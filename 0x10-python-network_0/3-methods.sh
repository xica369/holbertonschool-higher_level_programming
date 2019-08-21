#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size-body
curl -sI $1 | grep "Allow" | cut -d ":" -f2
