// https://projecteuler.net/problem=17
// Completed 1/19/2022

const numStr = ["null", "one", "two", "three", "four", "five", "six", "seven", "eight",
 "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
  "eighteen", "nineteen"];

const numStrTens = ["null", "null", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
"ninety"];

let sum = 0;

for(let current = 1; current <= 1000; current++){
  currentString = current.toString();
  if(currentString.length === 4){
    // Adding length of "One Thousand"
    sum += 11

  }else if(currentString.length === 3){ // 100-999
    //String segments of current number
    let currentSubOne = currentString.substring(0,1);
    let currentSubTwo = currentString.substring(1,2);
    let currentSubThree = currentString.substring(2,3);
    let currentSubTwoThree = currentString.substring(1,3);

    //Adding lenth of "Hundred"
    sum += 7;
    // Adding text length of first digit
    sum += numStr[parseInt(currentSubOne)].length;

    // Single digits and under 20
    if((parseInt(currentSubTwoThree) < 20) && (currentSubTwoThree !== "00")){
      sum += numStr[parseInt(currentSubTwoThree)].length;

      // Adding length of "and"
      sum += 3;

    }else if((parseInt(currentSubTwoThree) > 19) && (currentSubTwoThree !== "00")){
      sum += 3;

      if(currentSubThree === "0"){
        sum += numStrTens[parseInt(currentSubTwo)].length;

      } else if(currentSubTwo === "0"){
        sum += numStr[parseInt(currentSubThree)].length;

      } else {
        sum += numStrTens[parseInt(currentSubTwo)].length;
        sum += numStr[parseInt(currentSubThree)].length;
      }

    }

  }else if(currentString.length === 2){ // 10-99
    let currentSubOne = currentString.substring(0,1);
    let currentSubTwo = currentString.substring(1,2);

    // Adding single digits and under 20
    if(current < 20){
      sum += numStr[current].length;

    }else if(current < 100){
      
      if(currentSubTwo === "0"){
        sum += numStrTens[parseInt(currentSubOne)].length;

      } else if(currentSubTwo !== "0"){
      sum += numStrTens[parseInt(currentSubOne)].length;
      sum += numStr[parseInt(currentSubTwo)].length;
      }
    }

  }else{ // 1-9
    sum += numStr[current].length;
  }
}

console.log(sum);