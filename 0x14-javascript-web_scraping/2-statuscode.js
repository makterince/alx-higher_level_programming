#!/usr/bin/node
const request = require('request');
const requiredUrl = process.argv[2];

request.get(requiredUrl, function (error, response) {
  if (error) {
    console.error('Error: ', error);
  }
  console.log('code: ', response.statusCode);
});
