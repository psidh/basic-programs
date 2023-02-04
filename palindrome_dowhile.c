#include <stdio.h>

    int main(){
    int a , n , s=0, r;
    clrscr();
    printf("Enter the number :");
    scanf("%i", &n);
    a = n
    do {

        r = n%10;
        s = s*10 + r
        n = n/10
    }
    while(n>0);

    if (a == n){
        printf("Palindrome");
    
    } else {
        printf("Not a Palindrome");
    }
    return 0;
}