#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, text) {
  if (error) throw error;
  const d = JSON.parse(text);
  let g = 0;
  for (let i = 0; i < d.results.length; i++) {
    const characters = d.results[i].characters;
    if (characters.filter(str => str.includes('people/18/')).length !== 0) {
      g++;
    }
  }
  console.log(g);
});
