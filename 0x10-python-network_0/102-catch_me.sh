#!/bin/bash
# This sends a request to url and makes it respond with string
curl -sLX PUT 0.0.0.0:5000/catch_me_2 -H "Origin: School" -d "user_id=98"
