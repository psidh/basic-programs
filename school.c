#include <stdio.h>

int main()
{
    float maths, science, english, total, average, percentage;

    printf("Enter marks in Maths: ");
    scanf("%f", &maths);

    printf("Enter marks in Science: ");
    scanf("%f", &science);

    printf("Enter marks in English: ");
    scanf("%f", &english);

    total = maths + science + english;
    average = total / 3.0;
    percentage = (total / 300.0) * 100;

    printf("Total marks: %.2f\n", total);
    printf("Average marks: %.2f\n", average);
    printf("Percentage: %.2f\n", percentage);

    return 0;
}
