#!/usr/bin/node

const len = process.argv.length;
let myArr = [];
if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (let i = 0; i < (len - 2); i++) {
    myArr[i] = parseInt(process.argv[i + 2]);
  }
  myArr.sort();
  myArr.reverse();
  console.log(myArr[1]);
}
