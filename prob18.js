// https://projecteuler.net/problem=18
// Completed 2/22/2022

let list = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 04, 82, 47, 65, 19, 01, 23, 75, 03, 34, 88, 02, 77, 73, 07, 63, 67, 99, 65, 04, 28, 06, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 04, 62, 98, 27, 23, 09, 70, 98, 73, 93, 38, 53, 60, 04, 23];
let array = [];
let sum = 0;

// Triangle grid of numbers
for(let i = 0; i < 15; i++){
    array[i] = [];
}
for(let i = 0; i < 15; i++){
    for(let j = 0; j < i+1; j++){
        array [i][j] = list[j];
    }
    list.splice(0,i+1);
}

// Going from bottom up to find the largest sum path
// More efficient then brute force
for(let i = 13; i >= 0; i--){
    for(let j = 0; j < i+1; j++){
        let adjacent1 = array[i+1][j];
        let adjacent2 = array[i+1][j+1];

        if(adjacent1 >= adjacent2){
            array[i][j] += adjacent1;
        } else {
            array[i][j] += adjacent2;
        }
    }
}

console.log(array[0][0]);