#!/usr/bin/node

const list = require('./100-data.js').list;

const list2 = list.map(function (num, index) {
  return num * index;
});

console.log(list);
console.log(list2);
