#include <stdio.h>

int next_number(int num) {
  int sum = 0;
  while (num > 0) {
    int digit = num % 10;
    sum += digit * digit;
    num /= 10;
  }
  return sum;
}

int is_happy(int num) {
  int slow = num;
  int fast = num;
  do {
    slow = next_number(slow);
    fast = next_number(next_number(fast));
  } while (slow != fast);
  return slow == 1;
}

int main() {
  int num;
  printf("Enter a number: ");
  scanf("%d", &num);
  if (is_happy(num)) {
    printf("%d is a happy number.\n", num);
  } else {
    printf("%d is not a happy number
