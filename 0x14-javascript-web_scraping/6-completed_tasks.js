#!/usr/bin/node
// computes the number of tasks completed by user id.
// first argument is the API URL: https://jsonplaceholder.typicode.com/todos

const request = require('request');
console.log('{ ');
async function req () {
  for (let i = 1; i <= 10; i++) {
    const url = process.argv[2] + '?' + 'userId=' + i.toString();
    console.log(url);
    await request(url, postResponse);
  }
}
req();
function postResponse (error, response, body) {
  let n = 0;
  if (error) {
    return console.log(error);
  }
  else {
    const results = JSON.parse(body);
      for (let j = 0; j < results.length; j++) {
        if ((results[j]).completed === true) {
          console.log(results[j]);
	}
      }
  }
}
