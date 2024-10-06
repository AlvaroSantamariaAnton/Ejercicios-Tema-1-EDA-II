# Ejercicio 1 - Suma de Elementos en un Array

Este ejercicio implementa y compara dos soluciones para sumar todos los elementos de un array de enteros. Las soluciones utilizan diferentes enfoques para realizar la operación de suma, pero ambas tienen la misma complejidad temporal.

## Descripción del problema

Se tiene un array de enteros:

```python
lista_enteros = [1, 2, 3, 4, 5, 6]


def bucle_for():
    suma_total = 0
    for numero in lista_enteros:
        suma_total += numero
    print(f"La suma de todos los elementos de la lista es: {suma_total}")


def suma_funcion():
    suma_total = sum(lista_enteros)
    print(f"La suma de todos los elementos de la lista es: {suma_total}")