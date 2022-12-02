#!/usr/bin/node

let mySq = '';
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      mySq += 'X';
    }
    if (i < (num - 1)) {
      mySq += '\n';
    }
  }
  console.log(mySq);
}
