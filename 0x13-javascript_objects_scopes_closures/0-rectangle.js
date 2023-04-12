#!/usr/bin/node
class Rectangle {
	width;
	height;

	constructor(width, height) {
		this.width = width;
		this.height = height;
	}
	getArea() {
		console.log((this.width) * (this.height))
	};
}
