#!/usr/bin/node
const myNum = process.argv.splice(2);
const num = parseInt(myNum);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
