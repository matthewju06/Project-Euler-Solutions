// https://projecteuler.net/problem=9
let product;

for(let c = 0; c <= 1000; c++){
  for(let b = 0; b < c; b++){
    for(let a = 0; a < b; a++){

      // Checks that abc sum is 1000 and pythagorean is equal
      if((a + b + c === 1000) && (Math.pow(a, 2) + Math.pow(b, 2) === Math.pow(c, 2))){
        console.log(a);
        console.log(b);
        console.log(c);
        product = a * b * c;
      }
    }
  }
}

console.log(product);