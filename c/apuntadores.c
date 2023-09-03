#include<stdio.h>
#include<locale.h>
#include<langinfo.h>

int main(void){

    int var1 = 10;
    int *apEntero;
   
   apEntero = &var1;

    printf("El valor de var1 es: %d\n", var1);
    printf("El valor de *apEntero es: %d\n", *apEntero);
    printf("El valor de la direccion de memoria de apEntero es: %p\n", apEntero);
    printf("El valor de la direccion de memoria de var1 es: %p\n", var1);
    printf("El valor de la direccion de memoria al que apunta *apEntero o el contenido del apuntador *apEntero: %p\n", *apEntero);

    return 0;
}