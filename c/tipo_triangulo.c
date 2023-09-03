#include<stdio.h>

void calcula_tipo_triangulo(float *a, float *b, float *c){

    if(*a + *b <= *c || *a + *c <= *b || *b + *c <= *a){
        printf("Los datos ingresados no forman un tringulo!!!\n");
    } else if (*a == *b && *b == *c){
        printf("Los datos ingresados forman un triangulo equilatero\n");
    } else if (*a == *b || *a == *c || *b == *c){
        printf("Los datos ingresados forman un triangulo isosceles\n");
    } else {
        printf("Los datos ingresados forman un triangulo escaleno\n");
    }

}

int main(void){

    float lado1, lado2, lado3;

    printf("Programa que te dice que tipo de tringulo es de acuerdo al tamanio de sus lados.\n");

    printf("Ingresa el valor del lado 1:\n");
    scanf("%f", &lado1);
    printf("Ingresa el valor del lado 2:\n");
    scanf("%f", &lado2);
    printf("Ingresa el valor del lado 3:\n");
    scanf("%f", &lado3);
    
    calcula_tipo_triangulo(&lado1, &lado2, &lado3);
}