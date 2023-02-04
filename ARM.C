#include <stdio.h>
#include <math.h>

int isArmstrong(int num);

int main()
{
int num;
printf("To print whether the number is armstrong number.\n");
printf("Enter the number:\n");
scanf("%d", &num);


    if(isArmstrong(num))
    {
        printf("The entered number is an armstrong number.\n");
    }
    return 0;
}

int isArmstrong(int num) 
{
   int n=num,c=0,i,r,t,s=0,temp;
  t=num;
  temp=num;
  while(n!=0)
    {
      r=n%10;
      c++;
      n=n/10;
    }
  for(i=1;i<=c;i++)
    {
      r=t%10;
      s=s+pow(r,c);
      t=t/10;
    }
    
    return (temp == s);
}
