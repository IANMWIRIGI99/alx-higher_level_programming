#!/usr/bin/node
function factorial (x) {
  if (isNaN(x) || x === 1) {
    return (1);
  }
  return x * factorial(x - 1);
}
console.log(factorial(Number(process.argv[2])));
