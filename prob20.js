// https://projecteuler.net/problem=20
let sum = 0;
let bigNum = 1n;

// 100 factorial
for(let num = 100n; num > 0n; num --){
  bigNum = bigNum * num;
}

// Converting 100 factorial to string
let bigNumStr = bigNum.toString()

// Adding individual digits to total sum
for(let i = 0; i < bigNumStr.length -2; i ++){ 
  sum += parseInt(bigNumStr.substring(i,i+1))
}

console.log(sum);