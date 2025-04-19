# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    suma = 0
    for fila in matriz:
        for elemento in fila:
            suma += elemento
    return suma

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    maximo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento
    return maximo

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    
    else:
        primos_basicos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for primo in primos_basicos:
            if n in primos_basicos:
                return True
                break
            elif n % primo == 0:
                return False
                break
            elif n // primo < primo:
                return True  
                break

    

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la matriz transpuesta.
    Incluir el código aquí para transponer la matriz.
    """
    pass

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    """
    Recibe una lista de números y devuelve una nueva lista con solo los números pares.
    Incluir el código aquí para filtrar los números pares.
    """
    pass

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    """
    Recibe una frase y devuelve el número de palabras.
    Incluir el código aquí para contar las palabras en la frase.
    """
    pass

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    """
    Recibe un número y devuelve una lista con su tabla de multiplicar del 1 al 10.
    Incluir el código aquí para generar la tabla de multiplicar.
    """
    pass

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    """
    Recibe una lista de números y devuelve la cantidad de números negativos.
    Incluir el código aquí para contar los números negativos en la lista.
    """
    pass

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    """
    Recibe una lista de números y devuelve True si está ordenada de menor a mayor.
    Incluir el código aquí para verificar si la lista está ordenada.
    """
    pass

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
    pass


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()