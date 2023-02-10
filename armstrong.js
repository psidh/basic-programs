let readline = require('readline-sync');

let number = parseInt(readline.question("Enter a positive integer: "));

let originalNumber = number;
let n = 0;
let result = 0;

while (originalNumber !== 0) {
  originalNumber = Math.floor(originalNumber / 10);
  n++;
}

originalNumber = number;

while (originalNumber !== 0) {
  let remainder = originalNumber % 10;
  result += Math.pow(remainder, n);
  originalNumber = Math.floor(originalNumber / 10);
}

if (result === number) {
  console.log(`${number} is an Armstrong number.`);
} else {
  console.log(`${number} is not an Armstrong number.`);
}
