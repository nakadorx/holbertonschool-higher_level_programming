#!/usr/bin/node
const req = require('request');
let res = [];
req.get(process.argv[2], (error, respponse, body) => {

  if (error) {
    console.log(error);
  } else {
    res = JSON.parse(body).results;
  }
  let sum = 0;

  for (const m in res) {
    const chars = res[m].characters;
    for (const char in chars) {

      if (chars[char].endsWith('/18/')) {
        sum += 1;
      }
    }
  }

  console.log(sum);
});
