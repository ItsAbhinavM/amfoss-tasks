#include <stdio.h>

int main(void) {
    int max,i,j,count;
    int min=0;
    printf("Enter the number : ");
    scanf("%d",&max);
    for (i=min;i<=max;i++){
        int count=0;
        for (j=1;j<=i;j++){
            if (i%j==0){
                count++;
            }
        }
    if (count==2){
        printf("\n%d",i);
    }
    
    }
}