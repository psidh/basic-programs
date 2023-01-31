
#include <stdio.h>

int main()
{
    int i, start, end, sum=0;

    /* Input lower and upper limit from user */
    printf("Enter lower limit: ");
    scanf("%d", &start);
    printf("Enter upper limit: ");
    scanf("%d", &end);


    /* If start is not even then make it even */
    if(start%2 ==0)
    {
        start++;
    }

    for(i=start; i<=end; i+=2)
    {
        /* Add current even number to sum */
        sum += i;
    }

    printf("Sum of all even number between %d to %d = %d", start, end, sum);

    return 0;
}