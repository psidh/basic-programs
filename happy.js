function isHappy(num) {
  let slow = num;
  let fast = num;

  do {
    slow = nextNumber(slow);
    fast = nextNumber(nextNumber(fast));
  } while (slow != fast);

  return slow == 1;
}

function nextNumber(num) {
  let sum = 0;
  while (num > 0) {
    let digit = num % 10;
    sum += digit * digit;
    num = Math.floor(num / 10);
  }
  return sum;
}

console.log(isHappy(19));
