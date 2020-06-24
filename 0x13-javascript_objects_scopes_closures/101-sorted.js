#!/usr/bin/node

const firstDict = require('./101-data.js').dict;

const newDict = {};
let key;
let value;
for (key in firstDict) {
  value = firstDict[key];
  if (newDict[value] === undefined) {
    newDict[value] = [];
    newDict[value].push(key);
  } else {
    newDict[value].push(key);
  }
}
console.log(newDict);
