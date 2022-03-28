// https://projecteuler.net/problem=22
// Completed 3/28/2022

// Finding abundant numbers
let abundantNumbers = [];
for(let i = 0; i <= 28123; i++){
    let divSum = 0;
    for(let j = 1; j <= i/2; j++){
        if(i % j === 0){
            divSum += j;
        }
    }
    if(divSum > i){
        abundantNumbers.push(i);
    }
}

// Finding sums of abundants
let abundantSums = [];
for(let i = 0; i < abundantNumbers.length; i++){
    for(let j = 0; j < abundantNumbers.length; j++){
        abundantSums.push(abundantNumbers[i] + abundantNumbers[j]);
    }
}

// Finding integers that are not in the abundantSums list
let cannotSum = 0;
for(let i = 0; i <= 28123; i++){
    let validation = true;
    for(let j = 0; j < abundantSums.length; j++){
        if(i === abundantSums[j]){
            validation = false;
            break;
        }
    }
    if(validation === true){
        cannotSum += i;
    }
}

console.log(cannotSum);