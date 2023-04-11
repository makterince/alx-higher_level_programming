#!/usr/bin/node
function argumentChecker() {
	if (arguments.length === 0) {
		console.log('No argument');
	}
	else if (arguments.length === 1) {
		console.log('Argument found');
	}
	else {
		console.log('Arguments found');
	}
}
argumentChecker();
argumentChecker('Best');
argumentChecker('Best', 'School');
