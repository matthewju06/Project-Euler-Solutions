// https://projecteuler.net/problem=16
// Completed 1/5/2022

//2^1000 as big int so complete integer is displayed
let num = 2n ** 1000n;

//Converting num to string format for substring use
let numStr = num.toString();
let sum = 0;

for(let i = 0; i < numStr.length; i++){
    //Getting individual digits
    let temp = parseInt(numStr.substring(i,i+1))

    //Adding individual digits to sum
    sum += temp;
}

console.log(sum);