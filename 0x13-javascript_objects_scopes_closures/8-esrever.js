#!/usr/bin/node
exports.esrever = function (list) {
  const reverser = [];
  // loop through
  for (let i = list.length - 1; i >= 0; i--) {
    reverser.push(list[i]);
  }
  return reverser;
};
