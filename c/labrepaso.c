#include<stdio.h>
#include<stdlib.h>

void numero_mayor1(int *num1, int *num2, int *num3);
void numero_mayor2(int *num1, int *num2, int *num3, int *num4);
int numero_mayorN(int *num, int *mayor);
int menu();

int main(void){
        
    int opcion=0, num=1, num1=0, num2=0, num3=0, num4=0;
    int mayor=0;

    do{

        menu();
        scanf("%d", &opcion);
        switch (opcion){
            case 1:
                system("clear");
                printf("Ingresa el primer numero: ");
                scanf("%d", &num1);

                printf("Ingresa el segundo numero: ");
                scanf("%d", &num2);

                printf("Ingresa el tercer numero: ");
                scanf("%d", &num3);

                numero_mayor1(&num1,&num2,&num3);
                break;
            
            case 2:
                system("clear");
                printf("Ingresa el primer numero: ");
                scanf("%d", &num1);

                printf("Ingresa el segundo numero: ");
                scanf("%d", &num2);

                printf("Ingresa el tercer numero: ");
                scanf("%d", &num3);

                printf("Ingresa el cuarto numero: ");
                scanf("%d", &num4);

                numero_mayor2(&num1,&num2,&num3,&num4);
                break;

            case 3:
                system("clear");
                printf("Calcular el mayor de N numeros, [-1] para terminar\n");
                
                while (num != -1){
                    printf("Ingresa un numero: \n");
                    scanf("%d", &num);

                    numero_mayorN(&num,&mayor);

                }

                printf("El numero mayor es: %d\n", mayor);
                break;

            default:
                printf("Opcion incorrecta!!!\n");
                break;
        }

    } while (opcion != 4);
    
    return 0;

}

int menu(){
    printf("\nPor favor ingresa una opcion [1 - 4]:\n");
    printf("1.- Obtener el mayor de tres numeros enteros\n");
    printf("2.- Obtener el mayor de cuatro numeros enteros\n");
    printf("3.- Obtener el mayor de N numeros\n");
    printf("4.- Salir\n");
}

void numero_mayor1(int *num1, int *num2, int *num3){
    if (*num1 > *num2 && *num1 >= *num3){
        printf("\nEl numero mayor es el numero == %d ==\n", *num1);
    }
    else if (*num2 >= *num1 && *num2 > *num3){
        printf("\nEl numero mayor es el numero == %d ==\n", *num2);
    }
    else if (*num3 > *num1 && *num3 >= *num2){
        printf("\nEl numero mayor es el numero == %d ==\n", *num3);
    }
    else {
        printf("\nLos numeros son iguales!!!\n");
    }
}

void numero_mayor2(int *num1, int *num2, int *num3, int *num4){
    if (*num1 > *num2 && *num1 >= *num3 && *num1 >= *num4){
        printf("\nEl numero mayor es el numero == %d ==\n", *num1);
    }
    else if (*num2 >= *num1 && *num2 > *num3 && *num2 >= *num4){
        printf("\nEl numero mayor es el numero == %d ==\n", *num2);
    }
    else if (*num3 >= *num1 && *num3 >= *num2 && *num3 > *num4){
        printf("\nEl numero mayor es el numero == %d ==\n", *num3);
    }
    else if (*num4 > *num1 && *num4 >= *num2 && *num4 >= *num3){
        printf("\nEl numero mayor es el numero == %d ==\n", *num4);
    }
    else {
        printf("\nLos numeros son iguales!!!\n");
    }
}

int numero_mayorN(int *num, int *mayor){

    if (*mayor < *num){
        *mayor = *num;
    }

    return *mayor;
}