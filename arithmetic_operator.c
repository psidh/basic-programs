
#include<stdio.h>
 
int main()
{
  int x, y, *a, *b;
  int sum, mult, sub, div;

  printf("Enter the first number: ");
  scanf("%i", &x);
  printf("Enter the second number: ");
  scanf("%i", &y);
  
  a = *x;
  b = *y;

  sum = *a + *b;
  sub = *a - *b;
  mult = *a * *b;
  printf("%i", &sum)

  printf("%i", &sub)

  printf("%i", &mult)
  
  if (b == 0)
  {
    div = *a / *b
    printf("%i", div)
  }else if {
    printf("The denominator cannot be zero.")
  }
 
}