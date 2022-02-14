// https://projecteuler.net/problem=7
// Completed 12/25/2021

let primeNum = 2;
let currentNum = 5;
let primeCount = 0;


while(primeCount < 9999){
  let isPrime = true;
  for(let a = 2; a <= Math.round(Math.sqrt(currentNum)); a++){
    if(Number.isInteger(currentNum / a)){
      isPrime = false;
    }
  }
  if(isPrime){
      primeCount++;
      primeNum = currentNum;
      console.log(primeCount);
  }
  currentNum++;
}

console.log(primeNum);