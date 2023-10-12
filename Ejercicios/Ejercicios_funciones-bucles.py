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


def mcm(a, b):
    lista1 = []
    lista2 = []
    i = 1

    while True:
        lista1.append(str(a*i))
        lista2.append(str(b*i))
        for valores in lista2:
            if int(lista1[-1]) == int(valores):
                return int(valores)
        i += 1


num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
print(f'El Minimo común multiplo entre {num1} y {num2}, es :', mcm(num1, num2))

# 7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.


def area_tri(num1, num2):
    area = int(0.5*num1*num2)
    return (print(f'El área del triangulo de base {num1} y altura {num2}, es: ', area))


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


palabra = input(
    'escribe la palabra de la que quieres saber el numero de letras: ')

cuenta_palabra(palabra)


# 10. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.

def conversor_abs(lis):
    for contador in lis:
        lista_abs.append(abs(int(contador)))
    return (lista_abs)


lista_num = []
lista_abs = []
while True:
    num = input('Inserte los numeros de la lista y finalice con "fin" ')
    if num == 'fin':
        break
    lista_num.append(num)
print(
    f'El valor absoluto de la lista {lista_num}, es: ', conversor_abs(lista_num))


# 11. Crea una función que, dado un número, verifique si un número es primo.

# ya Realizado

# 12. Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.

def mcd(num1, num2):
    def Mayor(a, b):
        if a > b:
            return (a)
        else:
            return (b)

    def Menor(b):
        if b < Mayor(num1, num2):
            return (b)
        else:
            return (num1)

    ma = Mayor(num1, num2)
    me = Menor(num2)

    while me != 0:
        # print(f' 1ro ma es:{ma}, y me es:{me}')
        resto = ma % me
        if me % resto != 0:
            # print(f' 2ro me es:{me}, y resto es:{resto}')
            ma = resto
            me = me % resto
            # print(f' 3ro ma es:{ma}, y me es:{me}')
        else:
            break
    return (resto)


num1 = int(input('pon el primer numero: '))
num2 = int(input('pon el segundo numero: '))
print('el Maximo Comun Dividor es: ', mcd(num1, num2))
