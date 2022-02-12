// https://projecteuler.net/problem=10
let sum = 0;

for(let currentNum = 2; currentNum < 2000000; currentNum++){
  if(isPrime(currentNum)){
    sum += currentNum
  }
}

function isPrime(currentNum){ 
  for(let divisor = 2; divisor <= Math.round(Math.sqrt(currentNum)); divisor++){
    if(currentNum % divisor === 0){
      return false
    }
  }
  return true
}

console.log(sum)