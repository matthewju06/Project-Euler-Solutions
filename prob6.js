// https://projecteuler.net/problem=6
let sum1 = 0;
let difference;

for(let i = 1; i <= 100; i++){
  let newSquare;
  newSquare = i*i;
  sum1 = sum1 + newSquare;
}

let sum2 = 0;

for(let current = 1; current <= 100; current++){
  sum2 = sum2 + current;
}

sum2 = sum2 * sum2;

difference = sum1 - sum2;
console.log(difference);