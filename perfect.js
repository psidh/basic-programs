let num = 28;
let sum = 0;

for (let i = 1; i < num; i++) {
    if (num % i == 0) {
        sum += i;
    }
}

if (sum == num) {
    console.log(num + " is a perfect number.");
} else {
    console.log(num + " is not a perfect number.");
}
