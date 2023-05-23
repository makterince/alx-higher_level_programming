#!/usr/bin/node
const request = require('request');
const url = progress.argv[2];

request.get(url, function (error, response) {
  if (error) {
    console.error('Error: i', error);
  }
  console.log('code: ', response.statusCode);
});
