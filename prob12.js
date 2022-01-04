let currentNum = 1;
let nextNum = 2;
let largestDivCount = 0;
let largestNumber = 0;

while(largestDivCount < 500){ //
  let divCount = 0;
  let finalDivCount;
  let latestDiv;

  for(let i = 1; i <= Math.round(Math.sqrt(currentNum)); i++){ //Only finding sqrt of currentNum to save time instead of just going from 0 to currentNum as possible divisors
    if(currentNum % i === 0){
      latestDiv = i;
      divCount++
    }
  }

  if(Math.pow(latestDiv, 2) === currentNum){ //Decides true number of divisors since sqrt is not folly accurate
    finalDivCount = divCount * 2 - 1 //If number of divisors for currentNum is odd then that means currentNum * 2 - 1 is total number of divisors since currentNum can be squared
  }else{
    finalDivCount = divCount * 2 //If number of divisors for currentNum is even then that means currentNum * 2 is total number of divisors
  }

  if(finalDivCount > largestDivCount){
    largestDivCount = finalDivCount
    largestNumber = currentNum
  }

  currentNum += nextNum
  nextNum++
}

console.log(largestNumber)