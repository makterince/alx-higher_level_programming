#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const moviesWithWedge = films.filter((film) => {
      const characters = film.characters.map((characterUrl) => {
        return characterUrl.split('/').filter(Boolean).pop();
      });
      return characters.includes(characterId.toString());
    });
    console.log(moviesWithWedge.length);
  } else {
    console.error('Failed code:', response.statusCode);
  }
});
