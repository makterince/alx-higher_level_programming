#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request.get({ url, encoding: 'utf-8' }, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    // Write the response body to the file
    fs.writeFile(filePath, body, 'utf-8', function (err) {
      if (err) {
        console.error('Error writing file:', err);
      }
    });
  } else {
    console.error('Failed to retrieve webpage. Status code:', response.statusCode);
  }
});
