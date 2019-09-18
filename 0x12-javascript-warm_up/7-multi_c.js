#!/usr/bin/node
// prints x times C is fun
// If the first argument cant be converted to an integer, print Missing number of occurrences

function prints () {
  let cont = 0;
  if (parseInt(process.argv[2])) {
    for (cont = 0; cont < parseInt(process.argv[2]); cont++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
}

prints();
