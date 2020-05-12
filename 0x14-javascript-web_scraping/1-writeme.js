#!/usr/bin/node
const fileShare = require('fileShare');
fileShare.writeFile(process.argv[2], process.argv[3], 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
