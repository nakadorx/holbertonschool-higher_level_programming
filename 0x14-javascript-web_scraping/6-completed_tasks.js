#!/usr/bin/node
const req = require('request');
const doneT = {};
let tos;
req.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    tos = JSON.parse(body);
  }
  for (const i in tos) {
    const x = tos[i];
    if (x.completed === true) {
      if (!doneT[x.userId]) {
        doneT[x.userId] = 1;
      } else {
        doneT[x.userId]++;
      }
    }
  }
  console.log(doneT);
});
