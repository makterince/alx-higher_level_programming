#!/usr/bin/node
exports.Xtimes = function (x, theFunction) {
	for (let i = 0; i < x; i++) theFunction();
};
