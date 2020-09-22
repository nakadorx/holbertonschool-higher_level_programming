#!/usr/bin/node
const req = require('request');
req('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, response, body) => {
  (error) ? console.log(error) : console.log(JSON.parse(body).title);
});
