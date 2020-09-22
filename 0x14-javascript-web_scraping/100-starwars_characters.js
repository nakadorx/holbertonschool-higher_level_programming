#!/usr/bin/node
const req = require('request');
let res = [];
req.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, respponse, body) => {
  if (error) {
    console.log(error);
  } else {
    res = JSON.parse(body).characters;
  }
  for (const idCh in res) {
    req.get(res[idCh], (error, response, body) => {
      (error) ? console.log(error) : console.log(JSON.parse(body).name);
    });
  }
});
