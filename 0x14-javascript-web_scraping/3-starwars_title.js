#!/usr/bin/node
const request = require('request');
const episodeId = process.argv[2];
const apiUr = `https://swapi-api.alx-tools.com/api/films/${episodeId}`;
request.get(apiUr, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      console.log('Title:', movie.title);
    } else {
      console.error('failed code:', response.statusCode);
    }
});
