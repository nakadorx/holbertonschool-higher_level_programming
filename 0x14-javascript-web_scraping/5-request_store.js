#!/usr/bin/node
const fs = require('fs');
const req = require('request');
let res;
req.get(process.argv[2], (error, respponse, body) => {
  if (error) {
    console.log(error);
  } else {
    res = body;
  }
  fs.writeFile(process.argv[3], res, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
