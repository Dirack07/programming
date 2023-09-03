#include<stdio.h>


// enum deck{
//     club=0,
//     diamonds=5,
//     hearts=10,
//     spades=15,
// } card;

// int main(){

//     card = diamonds;
//     printf("Card Power: %d", card);
//     return 0;
// }

int main()

{

    int n = 1,mayor = 0;

    while (n != 0)

    {

        printf("\nIngresa un numero: ");

        scanf("%d",&n);

        if (mayor < n){

            mayor = n;

        }

    }

    printf("EL numero mayor es: %d",mayor);

    return 0;

}