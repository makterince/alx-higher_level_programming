#!/bin/bash
# Send an OPTIONS request to the URL and display the allowed methods
curl -sIX OPTIONS "$1" | grep -E "Allow: " | cut -d " " -f 2-
