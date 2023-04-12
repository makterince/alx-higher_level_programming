#!/usr/bin/node
class Rectangle {
	  constructor (w, h) {
		      if (w <= 0 || h <= 0) {
			      this.width = 0;
			      this.height = 0;
		      } else {
			      this.width = w;
			      this.height = h;
		      }
	  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
