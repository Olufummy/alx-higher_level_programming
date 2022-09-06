#!/usr/bin/node
exports.esrever = function (list) {
  let left = 0;
  let right = list.length - 1;

  while (left < right) {
    [list[left], list[right]] = [list[right], list[left]];
    left++;
    right--;
  }
  return list;
};
