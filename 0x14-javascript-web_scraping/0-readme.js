#!/usr/bin/node
fs.readFile('path/to/file.txt', 'utf8', (error, data) => {
	if (error) {
		console.error(error);
		return;
	}
	console.log(data);
}
);
