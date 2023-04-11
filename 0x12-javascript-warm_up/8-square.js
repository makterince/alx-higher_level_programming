#!/usr/bin/node
const Square = process.argv.splice(2);
const x = Square[0];
let i;
let j;
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (i = 0; i < x; i++) {
    let row = '';
    for (j = 0; j < x; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
