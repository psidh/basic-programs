const isNeon = (num) => {
  let square = num * num;
  let sum = 0;
  while (square > 0) {
    sum += square % 10;
    square = Math.floor(square / 10);
  }
  return sum === num;
};

const num = parseInt(prompt("Enter a number:"));
if (isNeon(num)) {
  console.log(num + " is a neon number.");
} else {
  console.log(num + " is not a neon number.");
}
