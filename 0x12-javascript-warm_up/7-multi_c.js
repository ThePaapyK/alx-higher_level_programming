#!/usr/bin/node

const myStr = 'C is fun';
let i = 0;
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of ocurrences');
} else {
  while (i < num) {
    console.log(myStr);
    i++;
  }
}
