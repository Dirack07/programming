#include<stdio.h>

int main(void){

    int miNumero = 10;
    int tamanioCadena = 10;
    char nombre[tamanioCadena];

    printf("Imprime el valor de la variable: %d\n", miNumero);
    
    //Imprimimos la direccion de memoria:
    printf("Imprimir la direccion de memoria: %p\n", &miNumero);

    printf("Proporciona un numero: \n");
    scanf("%d", &miNumero);

    printf("El numero proporcionado es: %d\n", miNumero);

    printf("Proporciona un nombre: \n");
    scanf("%[^'\n']s", nombre);

    printf("El nombre proporcionado es: %s", nombre);
    

    return 0;
}
