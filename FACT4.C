#include <stdio.h>

int main() {

    int n = 4;

    printf("The factorial of %d is %d",

    n, fact(n));

    return 0;

}

int fact(int x){


    return (x == 1 || x == 0)

    ? 1

    : x * fact(x - 1);

}