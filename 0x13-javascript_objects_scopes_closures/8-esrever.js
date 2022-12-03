#!/usr/bin/node

exports.esrever = function (list) {
  list.sort(function (a, b) { return (b - a) });
  return (list);
}
