#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const newList = [];
  for (let cont = list.length - 1; cont >= 0; cont--) {
    newList.push(list[cont]);
  }
  return (newList);
};
