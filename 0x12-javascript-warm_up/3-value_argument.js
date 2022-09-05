#!/usr/bin/node

const process = require('process');
const ag = process.argv[2];

if (ag) {
  console.log(ag);
} else {
  console.log('No argument');
}
