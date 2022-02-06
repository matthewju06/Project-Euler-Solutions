let array =[] 

for(let i = 0; i <= 20; i++){ //Creating a 21x21 2D array, extra 1 on top of 
                              // 20 to represent 1 at most right and bottom 
    array[i] = []
    for(let j = 0; j <= 20; j++){
        if(i === 20){   // Making bottom row all 1 because if you are at very 
                        // bottom there is only 1 solution (right) and very
                        // bottom right is 0 because that is the end meaning 
                        // nowhere else to go
            array[i][j] = 1;    
            array[i][20] = 0;
        }else if(j === 20){ // Making most right all 1 because if you are at 
                            // the very right you only have 1 solution (down)
            array[i][j] = 1;
        }else{
        array[i][j]= null;
        }
    }
}

for(i = 19; i >= 0; i--){   // The pattern is if you add the right and bottom 
                            // value of an unknown point then you can get the
                            // number of solutions you can go right and down to the end
    for(j = 19; j >= 0; j--){
        array[i][j] = array[i+1][j] + array[i][j+1]
    }
}


console.log(array[0][0]);