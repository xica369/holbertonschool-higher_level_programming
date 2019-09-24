#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  let cont = list.length - 1;
  const newList = [];
  while (cont) {
    newList.push(list[cont]);
    cont--;
  }
  newList.push(list[0]);
  return (newList);
};
