#!/usr/bin/node
// computes and prints a factorial
// The first argument is integer used for computing the factorial
// Factorial of NaN is 1

const factorial = function (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
};

const num = (parseInt(process.argv[2]));
try {
  console.log(factorial(num));
} catch (e) {
  console.log(factorial(1));
}
