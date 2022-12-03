#!/usr/bin/node

exports.esrever = function (list) {
  const rList = [];
  const index = list.length - 1;
  for (let i = index; i >= 0; i--) {
    rList.push(list[i]);
  }
  return (rList);
};
