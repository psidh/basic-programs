#include <stdio.h>
#include <math.h>


int main()


{int number; 
 
    

void arrayReadingData(const int sizeP) //array to read in the weight of the elephantseals
{
    
    
    FILE* in_file = fopen("name_of_file", "r"); // read only  
    
    if (! in_file ) // equivalent to saying if ( in_file == NULL ) 
        {  
        printf("oops, file can't be read\n"); 
        exit(-1); 
        } 

    // attempt to read the next line and store 
    // the value in the "number" variable 

   printf("Enter the weights into the array");
   for (i = 0; i < n; ++i)
   {
       printf("Enter weight %d: ", i+1);
       scanf("%f", &weight[i]);
       sum = sum + weight[i];
   }
   avg = sum / n;
   printf("Average weight for the set of the elephant seals. = %.4f units", avg);
   return 0;
}
}


int main(void)
{
    
    int size;
    printf("How many seals do you want to calculate the average weight for: ");
    scanf("%d", &size);

    arrayReadingData(size);
    printArray(size);
};

}
