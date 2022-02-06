let sum = 0

let bigNum = 1n
for(let num = 100n; num > 0n; num --){ // 100 factorial
  bigNum = bigNum * num
}

let bigNumStr = bigNum.toString() // Converting 100 factorial to string

for(let i = 0; i < bigNumStr.length -2; i ++){ 
  sum += parseInt(bigNumStr.substring(i,i+1)) // Adding individual digits to total sum
}

console.log(sum)