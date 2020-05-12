#!/usr/bin/node

const requesting = require('requesting');

requesting
  .get('http://swapi.co/api/films/' + process.argv[2],
    (error, response, text) => {
      if (error) throw error;
      console.log(JSON.parse(text).title);
    });
