// https://projecteuler.net/problem=15
let array =[];

//21x21 2D array to represent grid 
for(let i = 0; i <= 20; i++){
    array[i] = [];
    for(let j = 0; j <= 20; j++){
        // Bottom row all 1 b/c if at bottom, right is the only move 
        if(i === 20){   
            array[i][j] = 1;    
            array[i][20] = 0;

        // Making right all 1 b/c if at right, down is the only move
        }else if(j === 20){
            array[i][j] = 1;
        }else{
        array[i][j]= null;
        }
    }
}

// Pattern: if you add the right and bottom value of n then you get n
for(i = 19; i >= 0; i--){
    for(j = 19; j >= 0; j--){
        array[i][j] = array[i+1][j] + array[i][j+1];
    }
}

console.log(array[0][0]);