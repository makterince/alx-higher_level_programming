#!/bin/bash
# This sends a request and displays the response code
curl -s -o /dev/null -w %{http_code} $1
