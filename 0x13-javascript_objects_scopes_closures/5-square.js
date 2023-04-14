#!/usr/bin/node
// import rectangle
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
// export the square class
module.exports = Square;
