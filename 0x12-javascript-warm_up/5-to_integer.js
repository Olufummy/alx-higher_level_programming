#!/usr/bin/node

const ag = process.argv[2];
if (isNaN(ag)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(ag, 10));
}
