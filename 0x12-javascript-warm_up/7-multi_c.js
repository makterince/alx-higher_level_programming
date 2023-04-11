#!/usr/bin/node
const printX = process.argv.splice(2);
const x = printX[0];
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
