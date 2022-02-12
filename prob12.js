// https://projecteuler.net/problem=12

let currentNum = 1;
let nextNum = 2;
let largestDivCount = 0;
let largestNumber = 0;

while(largestDivCount < 500){
  let divCount = 0;
  let finalDivCount;
  let latestDiv;

  for(let i = 1; i <= Math.round(Math.sqrt(currentNum)); i++){
    if(currentNum % i === 0){
      latestDiv = i;
      divCount++;
    }
  }

  if(Math.pow(latestDiv, 2) === currentNum){
    finalDivCount = divCount * 2 - 1;
  }else{
    finalDivCount = divCount * 2;
  }

  if(finalDivCount > largestDivCount){
    largestDivCount = finalDivCount;
    largestNumber = currentNum;
  }

  currentNum += nextNum;
  nextNum++;
}

console.log(largestNumber);