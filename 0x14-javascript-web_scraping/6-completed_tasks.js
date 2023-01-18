#!/usr/bin/node
// computes the number of tasks completed by user id.
// first argument is the API URL: https://jsonplaceholder.typicode.com/todos

const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, function (error, request, body) {
  if (error) {
    console.log(err);
  } else {
    for (const item of JSON.parse(body)) {
      if (item.completed === true) {
        if (dict[item.userId]) {
          dict[item.userId]++;
        } else {
          dict[item.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
