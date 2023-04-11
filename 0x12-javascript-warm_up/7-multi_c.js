#!/usr/bin/node
const printX = process.argv.splice(2);
let x = printX[0];
let printInt = parseInt(x);
if (isNaN(x)) {
	console.log('Missing number of occurences');
}
else {
	for (i = 0; i < x; i++) {
		console.log('C is fun');
	}
}
