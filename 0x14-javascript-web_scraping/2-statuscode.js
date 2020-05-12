#!/usr/bin/node

const requesting = require('requesting');

requesting
  .get(process.argv[2])
  .on('response', (response) => {
    console.log('code:', response.statusCode);
  });
