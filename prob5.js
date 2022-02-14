// https://projecteuler.net/problem=5
// Completed 12/29/2021

let currentNumber = 1;
let dividend;
let dividendStatus = false;

while(dividendStatus === false){
  dividendStatus = true;
  for(let i = 1; i <= 20; i++){
    if(currentNumber % i === 0){
      dividendStatus = true;
    } else if (currentNumber % i !== 0){
      dividendStatus = false;
      i = 20;
    }
  }
  if(dividendStatus === true){
    dividend = currentNumber;
  }
  currentNumber++;
}

console.log(dividend);