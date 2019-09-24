#!/usr/bin/node
// class Rectangle that defines a rectangle
// The constructor must take 2 arguments w and h
// If w or h is equal to 0 or not a positive integer, create an empty object

const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
module.exports = Rectangle;
