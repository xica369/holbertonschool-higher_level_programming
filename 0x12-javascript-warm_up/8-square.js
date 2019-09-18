#!/usr/bin/node
// script that prints a square
// The first argument is the size of the square
// If the first argument cant be converted to an integer, print Missing size

function prints () {
  let size = 0;
  let cont1 = 0;
  let cont2 = 0;
  let print = 'X';

  if (parseInt(process.argv[2])) {
    size = parseInt(process.argv[2]);
    for (cont1 = 0; cont1 < size; cont1++) {
      for (cont2 = 1; cont2 < size; cont2++) {
        print = print + 'X';
      }
      console.log(print);
      print = 'X';
    }
  } else {
    console.log('Missing size');
  }
}

prints();
