#!/usr/bin/node
function increment(number, theFunction) {
	number++;
	theFunction(number);
}
exports.increment = increment;
