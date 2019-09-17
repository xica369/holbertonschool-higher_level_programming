#!/usr/bin/node
// prints two arguments passed to it - format: first arg "is" second arg
// If no arguments are passed to the script, print No argument

function prints () {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}

prints();
