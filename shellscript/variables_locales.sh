#!/bin/bash

mi_funcion() {
    variable_local="Hola, soy local"
    export variable_local
}

# Llamada a la función
mi_funcion

# Intenta acceder a la variable exportada fuera de la función
echo $variable_local