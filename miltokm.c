#include <stdio.h>

int main(void) {
	float miles;

	printf("Please enter miles:");
	scanf("%f", &miles);

	float kilometers = miles * 1.6;

	printf("%f Kilometers", kilometers);
}