#include <stdio.h>
int main() {

  int i, n;

  int t1 = 0, t2 = 1;

  int n3 = t1 + t2;

  printf("Enter the number of terms: ");
  scanf("%d", &n);

  printf("Fibonacci Series: %d, %d, ", t1, t2);

  for (i = 3; i <= n; ++i) {
    printf("%d, ", n3);
    t1 = t2;
    t2 = n3;
    n3 = t1 + t2;
  }

  return 0;
}
