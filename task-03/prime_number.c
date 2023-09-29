#include <stdio.h>

int main(void) {
    int upperLimit, i, j, isPrime;

    printf("Enter the maximum number: ");
    scanf("%d", &upperLimit);

    for (i = 2; i <= upperLimit; i++) {
        isPrime = 1; 

        for (j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                isPrime = 0; 
                break;
            }
        }

        if (isPrime) {
            printf("%d\n", i);
        }
    }

    return 0;
}
