#!/bin/bash
# Send a POST request to the URL with the email and subject variables
curl -s -X POST -d "email=$email&subject=$subject" $1
