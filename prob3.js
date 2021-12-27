let possible;
let correct;

for(let i = 0; i <= 775146.099225; i++){
  if(600851475143 % i === 0){
    let isPrime = true;
    possible = i
    for(let j = 2; j < possible; j++){
      if(possible % j === 0){
        isPrime = false;
      }
      
    }
    if(isPrime === true){
      correct = possible;
    }
  }
  
}

console.log(correct);