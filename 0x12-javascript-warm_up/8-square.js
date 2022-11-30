#!/usr/bin/node

let mySq = '';
const num = parseInt(process.argv[2]);
if (num > 0) {
  if (isNaN(num)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < num; i++) {
      for (let j = 0; j < num; j++) {
        mySq += 'x';
      } 
      if (i < (num - 1)) {
        mySq += '\n';
      }
    }
    console.log(mySq);
  }
}
