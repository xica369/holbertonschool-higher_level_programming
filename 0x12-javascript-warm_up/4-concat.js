#!/usr/bin/node
// prints the first argument passed to it
// If no arguments are passed to the script, print No argument

function prints () {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}

prints();
