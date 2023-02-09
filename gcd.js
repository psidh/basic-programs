function gcd(num1, num2) {
    if (num2 === 0) {
        return num1;
    }
    return gcd(num2, num1 % num2);
}

let num1 = parseInt(prompt("Enter first number: "));
let num2 = parseInt(prompt("Enter second number: "));
let result = gcd(num1, num2);
console.log(`The GCD of ${num1} and ${num2} is: ${result}`);
