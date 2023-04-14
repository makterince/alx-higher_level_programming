#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  // Loop through the list and increment the count each time the search element is found
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
