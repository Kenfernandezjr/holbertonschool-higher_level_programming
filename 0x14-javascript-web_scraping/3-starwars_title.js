#!/usr/bin/node

const request = require('request');
const urls = 'https://swapi-api.hbtn.io/api/films/';
const contact = process.argv[2];
const res = urls.concat(contact);

request.get(res, function (error, response, text) {
  if (error) throw error;
  console.log(JSON.parse(text).title);
});
