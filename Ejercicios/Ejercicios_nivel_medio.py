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

'''def conversor_binario(numero):
    numero_des = numero
    if numero == 0:
        return (print('El numero binario es 0'))
    while numero_des > 0:
        valor_binario = numero_des % 2
        numero_binario.append(valor_binario)
        numero_des = numero_des // 2
        # print(numero_des)
        # print(numero_binario)
    numero_binario.reverse()
    return (print(f'El numero {numero} en binario, es :', numero_binario))

numero_binario = []
numero = int(input('Inserte un numero: '))
conversor_binario(numero)'''

# 10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).

'''def lista_interseccion(lista1, lista2):
    contador = 0
    interseccion = []
    for i in lista1:
        for j in lista2:
            if j == i:
                interseccion.append(j)
    return (print('La lista con los elementos comunes de ambas listas ingresadas, Son: ', set(interseccion)))


lista1 = input('Inserte la primera lista de elementos: ')
lista2 = input('Inserte la segunda lista de elementos: ')
lista_interseccion(lista1, lista2)'''


# 11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

'''def palindromo(palabra):
    palabra_sin_espacios = [
        elemento for elemento in palabra if elemento.strip() != ""]
    palabra_min = [elemento.lower() for elemento in palabra_sin_espacios]
    contrario = palabra_min[::-1]

    if palabra_min == contrario:
        return (print(f'La frase "{palabra}", es un PALINDROMO'))


palabra_sin_espacio = []
pali = input('Inserte la primera para saber si es palindromo: ')
palindromo(pali)'''

# 12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.


'''def numeros_zz():
    for i in range(50):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

numeros_zz()'''

# 13. Ejercicio: Define una función que tome una lista y retorne la lista ordenadeda en orden ascendente.


'''def tipo_elementos(lista):
    cadena = 0
    entero = 0
    flotante = 0
    buleano = 0
    desconocido = 0

    for elemento in lista:
        if isinstance(elemento, str):
            cadena += 1
        elif isinstance(elemento, int):
            entero += 1
        elif isinstance(elemento, float):
            flotante += 1
        elif isinstance(elemento, bool):
            buleano += 1
        else:
            desconocido += 1

    if cadena == len(lista):
        return ('str')
    elif entero == len(lista):
        return ('int')
    elif flotante == len(lista):
        return ('float')
    elif buleano == len(lista):
        return ('bool')
    elif desconocido != 0:
        return ('desconocido')
    elif cadena != 0 or entero != 0 or flotante != 0:
        return ('mixto')
    else:
        return (print(f'La lista tiene {cadena} caracteres de tipo "str", {entero} de tipo "entero", {flotante} de tipo "flotante", {buleano} de tipo "buleano" y {desconocido} de tipo desconocido'))


def lista_ordenada(lista):
    if tipo_elementos(lista) == 'str':
        lista_min = [elemento.lower() for elemento in lista]
        lista_order = sorted(lista_min)
        return (print('La lista ordenada es: ', lista_order))
    elif tipo_elementos(lista) == 'int':
        lista_order = sorted(lista)
        return (print('La lista ordenada es: ', lista_order))
    elif tipo_elementos(lista) == 'float':
        lista_order = sorted(lista)
        return (print('La lista ordenada es: ', lista_order))
    elif tipo_elementos(lista) == 'desconocido':
        print('La lista tiene tipos de datos desconocidos')
    elif tipo_elementos(lista) == 'mixto':
        print('La lista tiene diferentes tipos de datos')


lista1 = ['a', 't', 'c', 'd', 'd', 'f', 'j', 'H', 'I', 'z', 'K', 'l', 'm']
lista2 = ['cuaderno', 'libro', 'lapiz', 'boli',
          'regla', 'Goma', 'Compás', 'cuter', 'lapiz']
lista3 = [64, 9874, 31, 321, 864, 87, 321, 3, 56, 489, 8,
          4, 5, 2, 1, 97, 88, 8, 6, 5, 2, 1, 4, 3, 65, 4, 2, 3]
lista4 = ['baba', 2, 'beso', 3, 'casa', 4, 'apio']


lista_ordenada(lista4)
'''

# version eficiente de chatGPT3
'''def tipo_elementos(lista):
    tipos = set(type(elemento) for elemento in lista)
    if len(tipos) == 1:
        if str in tipos:
            return 'str'
        elif int in tipos:
            return 'int'
        elif float in tipos:
            return 'float'
        elif bool in tipos:
            return 'bool'
    else:
        return 'mixto'


def lista_ordenada(lista):
    tipo = tipo_elementos(lista)
    if tipo == 'str':
        lista_ordenada = sorted(lista, key=str.lower)
        print('La lista ordenada es:', lista_ordenada)
    elif tipo == 'int' or tipo == 'float':
        lista_ordenada = sorted(lista)
        print('La lista ordenada es:', lista_ordenada)
    elif tipo == 'mixto':
        print('La lista tiene diferentes tipos de datos.')
    else:
        print('La lista está vacía o tiene tipos de datos desconocidos.')


# Ejemplos de listas
lista1 = ['a', 't', 'c', 'd', 'd', 'f', 'j', 'H', 'I', 'z', 'K', 'l', 'm']
lista2 = ['cuaderno', 'libro', 'lapiz', 'boli',
          'regla', 'Goma', 'Compás', 'cuter', 'lapiz']
lista3 = [64, 9874, 31, 321, 864, 87, 321, 3, 56, 489, 8,
          4, 5, 2, 1, 97, 88, 8, 6, 5, 2, 1, 4, 3, 65, 4, 2, 3]
lista4 = ['baba', 2, 'beso', 3, 'casa', 4, 'apio']

# Llamar a la función lista_ordenada con una lista específica
lista_ordenada(lista4)
'''

# 14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.

'''def lista_segun_numero(lista, numero):
    for palabra in lista:
        if len(palabra) > numero:
            lista_seleccion.append(palabra)
    print(lista_seleccion)


lista_seleccion = []
lista2 = ['cuaderno', 'libro', 'lapiz', 'boli',
          'regla', 'Goma', 'Compás', 'cuter', 'lapiz']
cantidad = int(
    input('cuantas letras como minimo desea que tengan las palabras? '))
lista_segun_numero(lista2, cantidad)'''


# 15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.

# ya realizado

# 16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
# ya realizado

# 17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.

'''def suma_numeros(numero):
    sum = 0
    for contador in str(numero):
        sum = sum + (int(contador)*int(contador)*int(contador))
    print('La suma de los numeros introducidos es', sum)


entrada = int(
    input('Ingrese un numero para que sus digitos al cubo sean sumados: '))
suma_numeros(entrada)'''

# 18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.

'''def busca_mayor(list):
    cont = 0
    for num in list:
        if num >= cont:
            cont = num
    return (cont)


def segundo_mayor(lista):
    cont2 = 0
    mayor = busca_mayor(lista)
    for valor in lista:
        if valor != mayor:
            if valor >= cont2:
                cont2 = valor

    print('el segundo numero mayor, es: ', cont2)


Lista = [2, 5, 6, 7, 8, 5, 4, 9, 5, 6, 2, 1, 3, 54, 4, 4, 2, 5, 6]
segundo_mayor(Lista)'''


# 19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.

'''def elemento_comun(lista1, lista2):
    global k
    for i in lista1:
        for j in lista2:
            if j == i:
                k += 1
    if k != 0:
        return (True)
    return (False)


k = 0
in_lista1 = input(
    'Agregue elementos para la lista 1 a comparar, separados por un espacio: ')
in_lista2 = input(
    'Agregar elementos para la lista 2 a comparar, separados por un espacio: ')


lista1 = [elemento.lower() for elemento in in_lista1.split()]
lista2 = [elemento.lower() for elemento in in_lista2.split()]

print("la lista1 es: ", lista1)
print("la lista2 es: ", lista2)

if elemento_comun(lista1, lista2):
    print(f"Las listas tienen {k} pares de coincidencia")
else:
    print("Las listas No tienen elementos en común")'''


# 20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
'''
def lista_inversa(lista):
    lista_inversa = lista[::-1]
    return (print(lista_inversa))


in_lista = input("ingrese una lista de elementos separados por un espacio: ")
lista = in_lista.split()
print(lista)
lista_inversa(lista)'''

# 21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.

'''def cuenta_elementos(cadena):
    i = 0
    j = 0
    for caracter in cadena:
        if caracter.isalpha():
            i += 1
        elif caracter.isdigit():
            j += 1
    print(f"la cadena tiene {i} letras y {j} números")

cadena = 'probando los numeros 3 4 y 5'
cuenta_elementos(cadena)'''


# 22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números

'''def suma_elementos(lista):
    suma_valor = 0
    for valor in lista:
        suma_valor = suma_valor + int(valor)
    return (print("la suma de los numeros de la lista es : ", suma_valor))


in_lista = input("Ingrese una lista de numeros separados por un espacio: ")
lista = in_lista.split()
suma_elementos(lista)'''

# 23. Ejercicio: Define una función que encuentre el elemento más común en una lista.

'''def mas_repetido(lista):
    for elemento in lista:
        if elemento in conteo_elementos:
            conteo_elementos[elemento] += 1
        else:
            conteo_elementos[elemento] = 1
    clave_maxima = max(conteo_elementos, key=conteo_elementos.get)
    print('El elemento mas repetido es: ', clave_maxima)


conteo_elementos = {}
in_lista = input("ingresa una lista de elementos separados por un espacio: ")
lista = in_lista.split()
mas_repetido(lista)'''

'''Se puede mejorar, analizando previamente si la cantidad de repetición de cada elemento  es la misma para todos los elementos de la lista, y  asi  decir que hay una cantidad igual  de cada elemento y  mostrar tambien cuantas veces es'''

# 24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.

'''def tabla_multiplicar(numero):
    multiplicacion = {}
    for i in range(10):
        multiplicacion[f'{numero} * {i+1}'] = (i+1) * numero
    for clave, valor in multiplicacion.items():
        print(f'{clave}: {valor}')


numero = int(input("indique que tabla de multiplicar decea: "))
tabla_multiplicar(numero)'''

# 25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.

'''def mas_repetido(lista):
    for elemento in lista:
        if elemento in conteo_elementos:
            conteo_elementos[elemento] += 1
        else:
            conteo_elementos[elemento] = 1
    print('Elementos y su cantidad de repetición')
    for elemento, conteo in conteo_elementos.items():
        print(f'{elemento}: {conteo}')


conteo_elementos = {}
in_lista = input("ingresa la cadena de texto de la que quiera cuantificar la cantidad de caracteres repetido: ")
lista = in_lista.split()
mas_repetido(lista)'''

# 26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
'''ATORADO'''
'''
def fun_lista_comun(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento2 == elemento1:
                lista_comun.append(elemento2)
    return (lista_comun)


def lista_no_comun(lista1, lista2, lista_comun):
    elemento = lista_comun[0]
    while elemento <= lista_comun[-1]:
        for elemento_c in lista_comun:
            for elemento1 in lista1:
                if elemento1 != elemento_c:
                    lista1_sin_lo_comun.append(elemento1)
    for elemento_c in lista_comun:
        for elemento2 in lista2:
            if elemento2 != elemento_c:
                lista2_sin_lo_comun.append(elemento2)
    lista_nocomun = lista1_sin_lo_comun + lista2_sin_lo_comun
    # print(lista_nocomun)

    print(lista1)
    print(lista2)
    print(lista_comun)
    print(lista1_sin_lo_comun)
    print(lista2_sin_lo_comun)


lista_comun = []
lista_nocomun = []
lista1_sin_lo_comun = []
lista2_sin_lo_comun = []

in_lista1 = input(
    'Ingrese la primera lista de elementos untilizando un espacio para separar: ')
lista1 = in_lista1.split()
in_lista2 = input(
    'ingrese la segunda lista de elementos untilizando un espacio para separar: ')
lista2 = in_lista2.split()

lista_no_comun(lista1, lista2, fun_lista_comun(lista1, lista2))'''


# 27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
'''
def lista_sinduplicado(lista):
    sin_duplicado = list(set(lista))
    print('La lista sin duplicados es: ', sin_duplicado)


lista = [2, 5, 6, 7, 8, 5, 4, 9, 5, 6, 2, 1, 3, 54, 4, 4, 2, 5, 6]
print('La lista completa es: ', lista)
lista_sinduplicado(lista)'''


# 28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.

'''def suma_con_limite(numero, limite):
    suma_elementos = 0
    for valor in numero:
        if int(valor) % 2 == 0:
            suma_elementos = suma_elementos + int(valor)**2
            # print(f'el valor es {valor} y la suma va en: ', suma_elementos)
        if int(valor) == limite:
            print(
                'La suma de los cuadrados de los numeros pares hasta el límite, es:', suma_elementos)


print('')
print('Esta función te devuelve la suma de los cuadrados de todos los números pares menores a un número límite')
print('')
numero = input('Ingrese el numero del que desea sumar sus dígitos: ')
limite = int(input('Ingrese un numero entero positivo como límite: '))
suma_con_limite(numero, limite)'''

# 29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.


'''def promedio_lista(lista):
    suma_total = 0
    contador = 0
    for valor in lista:
        suma_total = suma_total + int(valor)
        contador += 1
    print('Y el promedio es: ', (suma_total/contador))


lista = [2, 5, 6, 7, 8, 5, 4, 9]
print('La lista completa es: ', lista)

promedio_lista(lista)'''

# 30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.


'''def cadena_larga(lista):
    mayor = []
    for i in lista:
        for j in lista:
            if len(j) > len(i):
                mayor = j
    print('Y la cadena mas larga dentro de la lista, es :', mayor)


lista = ['once', 'doce', 'trece', 'catorce', 'quince']
print('La lista es: ', lista)
cadena_larga(lista)'''


# 31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.

'''def num_primo(num):
    for cont in range(2, int(num**0.5)+1):
        if num % cont == 0:
            return False
    return True


def primeros_n_primos(n):
    contador = 1
    lista_primos = [2]

    if n < 1:
        return (print('Debe colocar un número mayor a 1'))
    elif n == 1:
        return (print('El primer número primo es el: 2'))
    elif n > 1000:
        return (print('Elija un número menor a 1000'))
    else:
        for numero in range(3, 8001):
            if num_primo(numero):
                lista_primos.append(numero)
                contador += 1
                if contador == n:
                    return (print(f'Los {n} primeros números primos son: ', lista_primos))


print('Esta función entrega una lista con los primeros n numeros primeos que se le indiquen')
print('')
n = int(input('Indique cuantos numeros primeos quiere: '))
primeros_n_primos(n)'''

# 32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.

'''def cambio_de_orden(cadena):
    cadena_inversa = []
    cadena_inversa = cadena[::-1]
    print('Y la cadena invertida es: ', cadena_inversa)


cadena = 'La cadena de prueba es esta'
print('La cadena original es: ', cadena)
cambio_de_orden(cadena)'''

# 33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.


# 34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.


# 35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
