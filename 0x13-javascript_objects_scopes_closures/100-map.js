#!/usr/bin/node
const lst = require('./100-data').list;
console.log(lst);
const lst2 = lst.map((x, i) => x * i);
console.log(lst2);
