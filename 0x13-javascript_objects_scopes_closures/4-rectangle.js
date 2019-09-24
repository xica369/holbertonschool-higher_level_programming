#!/usr/bin/node
// class Rectangle that defines a rectangle
// The constructor must take 2 arguments w and h
// If w or h is equal to 0 or not a positive integer, create an empty object
// instance method called print() that prints the rectangle using character X
// method called rotate() that exchanges the width and the height of the rectan
// method called double() that multiples the width and height of the rectan * 2

const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let prints = '';
    for (let cont1 = 0; cont1 < this.height; cont1++) {
      for (let cont = 0; cont < this.width; cont++) {
        prints = prints + 'X';
      }
      console.log(prints);
      prints = '';
    }
  }

  rotate () {
    const tempH = this.height;
    this.height = this.width;
    this.width = tempH;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};

module.exports = Rectangle;
