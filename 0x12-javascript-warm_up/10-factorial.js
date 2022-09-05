#!/usr/bin/node

function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const ag = parseInt(process.argv[2], 10);

if (!ag) {
  console.log(1);
} else {
  console.log(factorial(ag));
}
