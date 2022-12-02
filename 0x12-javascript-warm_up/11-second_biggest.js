#!/usr/bin/node

const len = process.argv.length;
const myArr = [];
if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (let i = 0; i < (len - 2); i++) {
    myArr[i] = parseInt(process.argv[i + 2]);
  }
  myArr.sort(function (a, b) { return b - a; });
  console.log(myArr[1]);
}
