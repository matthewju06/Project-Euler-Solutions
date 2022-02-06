let num = 2n ** 1000n //2^1000 as big int so complete integer is displayed
let numStr = num.toString() //Converting num to string format so substring can be used in loop below
let sum = 0;

for(let i = 0; i < numStr.length; i++){
    let temp = parseInt(numStr.substring(i,i+1)) //Getting individual digits and converting back to integer
    sum += temp //Adding individual digits together
}

str = sum.toString()

console.log(str);