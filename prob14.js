// https://projecteuler.net/problem=14

let newNum = 0;;
let largestChain = 0;
let largestNum = 0;

for(let current = 1; current < 1000000; current++){
  let chainLength = 0;
  newNum = current;
  while(newNum !== 1){
    if(newNum % 2 === 0){
      newNum = newNum / 2;
      chainLength++;
    }else{
      newNum = newNum * 3 + 1
      chainLength++;
    }
  }
  if(chainLength > largestChain){
    largestNum = current;
    largestChain = chainLength;
  }
}

console.log(largestNum);