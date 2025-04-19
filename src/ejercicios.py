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
    fil = len(matriz)
    col = len(matriz[0])

    transpuesta = []
    for j in range(col):
        nueva_fila = []
        for i in range(fil):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)
    return transpuesta

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    lista_par = []
    for num in lista:
        if num % 2 == 0:
            lista_par.append(num)
    return lista_par

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    cont = 0
    palabra = frase.split()
    for i in palabra:
        cont +=1
    return cont


# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    cont = 1
    lista_tabla = []
    while cont <= 10:
        lista_tabla.append(n*cont)
        cont += 1
    return lista_tabla


# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    cont = 0
    for num in lista:
        if num < 0:
            cont += 1
    return cont

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    cont = len(lista)-1
    for i in range(cont):
        if lista[i] > lista[i+1]:
            return False
                 
    return True

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