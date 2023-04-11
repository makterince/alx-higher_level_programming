#!/usr/bin/node
function Xtimes(x, theFunction) {
	for (let i = 0; i < x; i++) {
		return (theFunction());
	}
};
module.exports.Xtimes = Xtimes;
