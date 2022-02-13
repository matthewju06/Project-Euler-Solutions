// https://projecteuler.net/problem=1
// Completed 12/29/2021

let sum = 0;
let dividend = 1;
let secondSum = 0;
let secondDividend = 0;

while(dividend < 1000){
  if(dividend % 3 === 0){
    sum = sum + dividend;
  }
  if(dividend % 5 === 0){
    sum = sum + dividend;
  }
  dividend++;
}

while(secondDividend < 1000){
  if(secondDividend % 5 === 0){
    secondSum = secondSum + secondDividend;
  }
  secondDividend = secondDividend + 15;
}

console.log(sum - secondSum);