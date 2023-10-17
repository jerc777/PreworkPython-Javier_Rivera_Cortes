# Ejercicios nivel medio
# 1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros nnúmeros de la serie de Fibonacci.

'''def serie_fibonacci(can):
    lista = [1, 1]
    if can == 1:
        lista = [1]
        return (print('El valor de la serie es :', lista))
    elif can == 2:
        lista = [1, 1]
        return (print('El valor de la serie es :', lista))
        
    elif can!=1 and can!=2:
        h = 0
        i = 1
        j = 1
        contador = 0
        while contador < (can-2):
            h = i+j
            i = j
            j = h
            lista.append(h)
            contador += 1
        return (print('El valor de la serie es :', lista))


cantidad = int(input('Indique cuantos numero de la serie fibonacci quiere: '))
serie_fibonacci(cantidad)'''

# 2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.


'''def divisores_num(num):
    contador = 1
    lista = []
    while contador <= num:
        if num % contador == 0:
            lista.append(contador)
        contador += 1
    return (print(f'Los divisores de {num} son: ', lista))


cantidad = int(input('Indique un numero para saber sus divisores: '))
divisores_num(cantidad)'''

# 3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.

'''
def extractor_base(lista):
    lista_1 = []
    lista_2 = []
    for indice_i, valor_i in enumerate(lista):
        lista_1 = lista[1:]
        for indice_j, valor_j in enumerate(lista_1):
            if valor_j != valor_i:
                lista_2.append(valor_j)
    return (lista_base)


lista_num = []
while True:
    num = input('Inserte los numeros de la lista y finalice con "fin" ')
    if num == 'fin':
        break
    lista_num.append(num)
extractor_base(lista_num)'''

# tambien se puede utilizar el sistema llamado "lista de comprensión"

# 4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.

# ya realizaodo

# 5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.

'''def cuenta_vocal(lista):
    contador = 0
    vocales = ['a', 'e', 'i', 'o', 'u']
    lista_minuscula = [elemento.lower() for elemento in lista]
    for i in vocales:
        for j in lista_minuscula:
            if j == i:
                contador += 1
    return (print(f'La frase: "{lista}", tiene {contador} vocales'))


lista = input('Inserte la frase de la que quiera saber cuantas vocles tiene: ')
cuenta_vocal(lista)'''

# 6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.

'''def recuperar_lista(lista, n):

    i = 0
    # while indice <= n:
    for indice, valor in enumerate(lista):
        if indice != n:
            print(f'El indice es {indice}, y el valor es {valor}')
            lista_recuperada.append(valor)
        elif indice == n:
            return (print('los elementos recuperados son: ', lista_recuperada))


lista_recuperada = []
lista = input('Inserte una lista de elemenetos: ')
n = int(input('indique cuantos elementos quiere recuperar, recuerde contavilizar los espacios: '))
recuperar_lista(lista, n)'''

# 7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.


'''def mayusculas_minusculas(lista):
    mayusculas = 0
    minusculas = 0
    for indice, valor in enumerate(lista):
        if valor.isupper():
            mayusculas += 1
        else:
            minusculas += 1
    return (print(f'La frase "{lista}", tiene {mayusculas} mayusculas y {minusculas} minusculas'))

lista = input('Inserte una frase: ')
mayusculas_minusculas(lista)'''


# 8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.

'''def divisores_num(num):
    contador = 1
    lista = []
    while contador <= num:
        if num % contador == 0:
            lista.append(contador)
        contador += 1
    return (lista)

def suma_numeros(num):
    sum = 0
    for contador in num:
        sum = sum + int(contador)
    return (sum-int(num[-1]))

def perfecto(num):
    divisores = divisores_num(num)
    suma = suma_numeros(divisores)
    # print(f'el numero es {num}, el divisores {divisores}, la suma {suma}')
    if num == suma:
        return (print('El numero si es Perfecto'))
    else:
        return (print('El numero no es Perfecto'))


num = int(input('Indique el numero del que quiere saber si es Perfecto: '))
perfecto(num)'''

# 9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.


# 10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).


# 11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).


# 12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.


# 13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.


# 14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.


# 15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.


# 16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.


# 17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.


# 18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.


# 19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.


# 20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.


# 21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.


# 22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números


# 23. Ejercicio: Define una función que encuentre el elemento más común en una lista.


# 24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.


# 25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.


# 26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.


# 27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.


# 28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.


# 29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.


# 30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.


# 31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.


# 32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.


# 33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.


# 34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.


# 35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
