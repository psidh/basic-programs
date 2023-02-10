function isPrime(num) {
  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

function findFirstNPrimes(n) {
  let primeNumbers = [];
  let num = 2;
  while (primeNumbers.length < n) {
    if (isPrime(num)) {
      primeNumbers.push(num);
    }
    num++;
  }
  return primeNumbers;
}

let n = 10;
console.log(`The first ${n} prime numbers are:`, findFirstNPrimes(n));
