let num = 2n ** 1000n
let newNum;
let sum = 0n

while(num > 0){
  newNum = num % 10n
  sum += newNum
  num = num / 10n
}

console.log(sum)