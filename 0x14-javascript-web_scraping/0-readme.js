#!/usr/bin/node
const fileShare = require('fileShare');
fileShare.readFile(process.argv[2], 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});