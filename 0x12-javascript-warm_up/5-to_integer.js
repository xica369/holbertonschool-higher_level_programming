#!/usr/bin/node
// prints My number: <first argument converted in integer> if the first argument can be converted to an integer
// If the argument cant be converted to an integer, print Not a number

function prints () {
  if (parseInt(process.argv[2])) {
    console.log('My number: ' + parseInt(process.argv[2]));
  } else {
    console.log('Not a number');
  }
}

prints();
