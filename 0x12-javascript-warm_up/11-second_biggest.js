#!/usr/bin/node

const arg = process.argv;

if (arg.length < 4) {
  console.log(0);
} else {
  const listInt = [];
  arg.forEach((val, index) => {
    if (index >= 2) {
      listInt.push(parseInt(val, 10));
    }
  });

  listInt.sort((a, b) => a - b);
  console.log(listInt[listInt.length - 2]);
}
