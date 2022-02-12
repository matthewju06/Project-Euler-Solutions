// https://projecteuler.net/problem=21
let sum = 0;

for(let numA = 1; numA < 10000; numA++){
  let numB = 0;
  let numBReverse = 0;

  // Finding sum of divisors of i
  for(let j = 1; j <= numA/2; j++){
    if(numA % j === 0){
      numB += j;
    }
  }

  // Finding sum of divisors of numB
  for(let j = 1; j <= numB/2; j++){
    if(numB % j === 0){
      numBReverse += j;
    }
  }

  // If numA is equal to numB divisors sum
  // And if numA is not equal to numB
  if(numA === numBReverse && numA !== numB){
    sum += numA;
    }
}

console.log(sum);