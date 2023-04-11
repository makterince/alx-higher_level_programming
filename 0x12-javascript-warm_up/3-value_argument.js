#!/usr/bin/node
const printFirst = process.argv.splice(2);
if (printFirst[0]) {
	console.log(printFirst[0]);
}
else {
	console.log('No argument');
}
