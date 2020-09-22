#!/usr/bin/node
const req = require('request');
let charac;
const nameso = {};
req.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, respponse, body) => {
  if (error) {
    console.log(error);
  } else {
    charac = JSON.parse(body).characters;
  }
  for (const id of charac) {
    req.get(id, (error, response, body) => {
      if (!error) {
        nameso[id] = JSON.parse(body).name;
        if (Object.values(nameso).length === charac.length) {
          for (const id of charac) {
            console.log(nameso[id]);
          }
        }
      }
    });
  }
});
