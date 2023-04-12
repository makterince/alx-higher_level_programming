#!/usr/bin/node
class Rectangle {
	width;
	height;

	constructor(width, height) {
		this.width = width;
		this.height = height;
	}
	getArea() {
		return ((this.width) * (this.height));
	}
}
