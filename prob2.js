let sumEvens = 0;
let previousNumberSmall = 1
let previousNumberBig = 2
let current = 0;

while(current < 4000000){
  current = previousNumberSmall + previousNumberBig;
  if(current % 2 === 0){
    sumEvens = sumEvens + current;
  }
  previousNumberSmall = previousNumberBig;
  previousNumberBig = current;
}
sumEvens = sumEvens + 2;
console.log(sumEvens);