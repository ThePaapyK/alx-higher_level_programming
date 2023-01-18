#!/usr/bin/node
// prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const id = 'https://swapi-api.alx-tools.com/api/people/18/';
let n = 0;
request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const films = JSON.parse(body).results;
  for (let i = 0; i < films.length; i++) {
    if ((films[i].characters).includes(id)) {
      n++;
    }
  }
  console.log(n);
});
