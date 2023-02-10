function fibonacci(n) {
  if (n <= 0) return 0;
  if (n == 1) return 1;

  let prev = 0;
  let curr = 1;
  let next;
  let i = 2;
  let res = [prev, curr];

  while (i <= n) {
    next = prev + curr;
    prev = curr;
    curr = next;
    res.push(curr);
    i++;
  }

  return res;
}

console.log(fibonacci(10));
