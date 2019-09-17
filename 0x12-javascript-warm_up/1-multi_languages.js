#!/usr/bin/node
// script that prints 3 lines:
// The first line: C is fun
// The second line: Python is cool
// The third line: Javascript is amazing

function prints () {
  const list = ['C is fun', 'Python is cool', 'Javascript is amazing'];
  for (let cont = 0; cont < 3; cont++) {
    console.log(list[cont]);
  }
}

prints();
