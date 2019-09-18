#!/usr/bin/node
// searches the second biggest integer in the list of arguments.
// If no argument passed, print 0
// If the number of arguments is 1, print 0

function second_biggest () {
  const list = [];
  let cont = 2;
  if (process.argv.length === 2 || process.argv.length === 3) {
    console.log(0);
  } if (process.argv.length > 3) {
    while (process.argv[cont]) {
      list.push(parseInt(process.argv[cont]));
      cont++;
    }
  }
  list.sort((a, b) => a - b);
  console.log(list[list.length - 2]);
}

second_biggest();
