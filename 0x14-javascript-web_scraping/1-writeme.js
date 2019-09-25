#!/usr/bin/node
// script that writes a string to a file
// The first argument is the file path
// The second argument is the string to write
// If an error occurred during while writing, print the error object

const fs = require('fs');
const file = process.argv[2];
const write_ = process.argv[3];

fs.writeFile(file, write_, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
