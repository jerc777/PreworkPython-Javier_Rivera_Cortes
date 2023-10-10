'''
# 1. Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.
# ya Realizado

# 2. Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.
# Ya realizado

# 3. Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.
# PISTA: Para convertir un número a string usa el método str(). Te recordamos que para saber la longitud de una cadena utilizamos len()

a = input('Ingrese un numero para saber cuantos digitos tiene: ')
print(f'El número {a}, tiene {len(str(a))} digitos')

# 4. Dada una lista de números, crea una función que devuelva el número máximo de la lista.


def busca_mayor(list):
    cont = 0
    for num in list:
        if num >= cont:
            cont = num
    print('El numero mayor es el: ', cont)

Lista = [2, 5, 6, 7, 8, 5, 4, 9, 5, 6, 2, 1, 3, 54, 4, 4, 2, 5, 6]
busca_mayor(Lista)

# 5. Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.

def suma_numeros(cond1):
    sum = 0
    for contador in str(cond1):
        sum = sum + int(contador)
    print('La suma de los numeros introducidos es', sum)


entrada = int(input('Ingrese un numero para que sus digitos sean sumados: '))
suma_numeros(entrada)

# 6. Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.

# 7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.


def area_tri(num1, num2):
    area = int(0.5*num1*num2)
    return (print(f'El área del triangulo de base {num1} y altura {num2}, es: ',area))


base = int(input('Ingresa la base del triangulo: '))
altura = int(input('ingresa la altura del triangulo: '))
area_tri(base, altura)

# 8. Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.

def num_pnc(num):
    if num < 0:
        return (print('El numero es Negativo'))
    elif num > 0:
        return (print('El numero es Positivo'))
    elif num == 0:
        return (print('El numero es Cero'))


pnc = int(input('indique el numero para saber si positivo, negativo o cero: '))
num_pnc(pnc)


# 9. Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.

def cuenta_palabra(pal):
    contador = 0
    for num in pal:
        contador += 1
    return (print(contador))


palabra = input('escribe la palabra de la que quieres saber el numero de letras: ')

cuenta_palabra(palabra)

'''
# 10. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.


def val_abs(numeros):
    lista_abs = []
    for recorrido in numeros:
        if int(recorrido) < 0:
            lista_abs.append(abs(int(recorrido)))
        else:
            lista_abs.append(int(recorrido))
    return lista_abs


entrada_usuario = input(
    'Inserte una lista de numeros separados por una coma: ')
# Convierte la entrada en una lista de cadenas
numeros_texto = entrada_usuario.split(',')

# Convierte cada cadena en la lista a un número entero
numeros_enteros = [int(numero) for numero in numeros_texto]

numeros_absolutos = val_abs(numeros_enteros)
print('El valor absoluto de la lista de numeros es:', numeros_absolutos)


# 11. Crea una función que, dado un número, verifique si un número es primo.

# ya Realizado

# 12. Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.
