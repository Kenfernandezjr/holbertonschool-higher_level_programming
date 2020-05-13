#!/usr/bin/node

const request = require('request');

request
  .get(process.argv[2],
    (error, response, text) => {
      if (error) throw error;
      console.log(JSON.parse(text).title);
    });
