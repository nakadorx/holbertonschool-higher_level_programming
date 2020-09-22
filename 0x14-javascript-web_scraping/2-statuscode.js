#!/usr/bin/node
const req = require('request');
req(process.argv[2], (error, response, body) => {
  (error) ? console.log(error) : console.log('code: ' + response.statusCode);
});
