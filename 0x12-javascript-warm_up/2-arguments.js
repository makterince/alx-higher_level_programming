#!/usr/bin/node
const argumen = process.argv.slice (2);
	if (argumen.length === 0) {
		console.log('No argument');
	}
	else if (argumen.length === 1) {
		console.log('Argument found');
	}
	else	console.log('Arguments found');
