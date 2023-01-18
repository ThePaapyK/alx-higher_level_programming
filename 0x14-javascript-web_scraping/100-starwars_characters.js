#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  for (const charac of JSON.parse(body).characters) {
    request(charac, function (error, response, body) {
      if (error) {
        return console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
