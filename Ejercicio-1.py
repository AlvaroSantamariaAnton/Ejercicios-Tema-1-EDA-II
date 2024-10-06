# EJERCICIO 1 - SUMA DE ELEMENTOS EN UN ARRAY

lista_enteros = [1, 2, 3, 4, 5, 6]

# Solucion 1 - Bucle for para iterar
"""
En este caso la complejidad temporal es O(n),
donde n = 6, por lo tanto O(6)
"""
def bucle_for():
    suma_total = 0

    for numero in lista_enteros:
        suma_total += numero
        
    print(f"La suma de todos los elementos de la lista es: {suma_total}")


# Solucion 2 - Funcion sum()
"""
En este caso la complejidad temporal es O(n),
donde n = 6, por lo tanto O(6)
"""
def suma_funcion():
    suma_total = sum(lista_enteros)

    print(f"La suma de todos los elementos de la lista es: {suma_total}")


# Ejecutar las funciones
bucle_for()
suma_funcion()


# ¿Cuál es más eficiente?
"""
A nivel de complejidad temporal, la función sum() también recorre cada elemento del array una vez.
Por lo tanto, su complejidad temporal es la misma que en la Solución 1: O(n),
donde n es el número de elementos en el array.
"""

# Comparación de las soluciones
"""
Solución 1 (bucle for): Más control sobre cada paso de la suma, útil si necesitas hacer algo más dentro del bucle.
Solución 2 (sum()): Más simple y concisa, especialmente cuando no necesitas realizar otras operaciones durante la suma.
"""

# Conclusión final
"""
En resumen, aunque la complejidad temporal es la misma, sum() es mejor opción si buscas simplicidad, legibilidad, y evitar pasos extra.
"""