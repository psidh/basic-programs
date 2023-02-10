#include <stdio.h>
int main(){
    int a , b, r;
    printf("Enter number 1: ");
    scanf("%i", &a);
    printf("Enter nu ber 2: ");
    scanf("%i", &b);
    
    while (b != 0){
        r = a %b;
        a = b;
        b = r;

    }
    printf("GCD of the two is: %i" , r)
    // return 0;
}
