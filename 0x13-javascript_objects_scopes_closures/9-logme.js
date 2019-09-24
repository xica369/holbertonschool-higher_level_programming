#!/usr/bin/node
// prints the number of arguments already printed and the new argument value.

let cont = 0;

exports.logMe = function (item) {
  console.log(cont + ': ' + item);
  cont++;
};
