#include<stdio.h>

void findFact(int,int *);

int main(){

    int x,fact,n;

    printf("Enter a number to get factorial: ");

    scanf("%d",&n); 

    findFact(n,&fact);

    printf("The factorial of %d is: %d",n,fact); 

    return 0;

} 

void findFact(int n,int *fact){

    int x;

    *fact =1;

    for(x=1;x<=n;x++)

        *fact=*fact*x;

}