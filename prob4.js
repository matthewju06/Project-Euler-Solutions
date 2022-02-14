// https://projecteuler.net/problem=4
// Completed 12/29/2021

let firstNumber = 100;
let secondNumber = 100;
let product;
let str;
let sub;
let newbiggestPalindrome;
let biggestPalindrome = 0;

while(firstNumber < 1000){
    while(secondNumber < 1000){
        product = firstNumber * secondNumber;

        str = product.toString();

        if(product > 99999){
            let sixDigOne = str.substring(0,1);
            let sixDigTwo = str.substring(1,2);
            let sixDigThree = str.substring(2,3);
            let sixDigFour = str.substring(3,4);
            let sixDigFive = str.substring(4,5);
            let sixDigSix = str.substring(5,6);

            if((sixDigOne === sixDigSix) && (sixDigTwo === sixDigFive) && (sixDigThree === sixDigFour)){
                newbiggestPalindrome = product;

                if(newbiggestPalindrome > biggestPalindrome){
                    biggestPalindrome = newbiggestPalindrome;
                }
            }
        }else{
            let sixDigOne = str.substring(0,1);
            let sixDigTwo = str.substring(1,2);
            let sixDigFour = str.substring(3,4);
            let sixDigFive = str.substring(4,5);

            if((sixDigOne === sixDigFive) && (sixDigTwo === sixDigFour)){
                newbiggestPalindrome = product;

                if(newbiggestPalindrome > biggestPalindrome){
                    biggestPalindrome = newbiggestPalindrome;
                }
            }
        }

        secondNumber++;
        
    }
    secondNumber = 100;
    firstNumber++;
}

console.log(biggestPalindrome);