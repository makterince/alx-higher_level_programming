#!/bin/bash
# Send an OPTIONS request to the URL and display the allowed methods
curl -s -X OPTIONS -i $1 | grep "Allow:" | tr -d '\r\n' | sed 's/Allow: //'
