#!/usr/bin/node
function Xtimes(x, theFunction) {
	if (x <= 0 ) {
		return ;
	}
	theFunction();
	Xtimes(x - 1, theFunction);
}
module.exports.Xtimes = Xtimes;
