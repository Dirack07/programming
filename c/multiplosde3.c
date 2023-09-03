#include <stdio.h>

int main(void){

    int i = 0;

    printf("Los multiplos de 3 entre -15 y -3 son: \n");
    for (i = -15; i <= -3; i++)
    {
        if(i%3 == 0){
            printf("%d ", i);
        }
    }
    printf("\n");

    return 0;

}