#!/usr/bin/node

const ag = parseInt(process.argv[2], 10);

if (!ag) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < ag; i++) {
    console.log('C is fun');
  }
}
