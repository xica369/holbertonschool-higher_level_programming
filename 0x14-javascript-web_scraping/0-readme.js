#!/usr/bin/node
// script that reads and prints the content of a file
// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', (error, datos) => {
  if (error) {
    console.log(error);
  } else {
    console.log(datos);
  }
});
