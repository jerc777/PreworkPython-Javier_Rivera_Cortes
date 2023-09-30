
# 1. Ejercicio: Dado un número, imprime si es positivo o negativo.

def positivo_negativo(num):
    if num < 0:
        print(f'El número {num} es Negativo')

    elif num == 0:
        print(f'El número {num} es Cero')
    elif num > 0:
        print(f'El número {num} es Positivo')


num1 = int(input("Ingrese un numero para saber si es positivo o negativo: "))
positivo_negativo(num1)

# 2. Ejercicio: Dado un número, imprime si es par o impar.


def par_impar(num):
    a = num % 2
    if a == 0:
        print(a)
        print(f'El número {num} es es par')

    else:
        print(f'El número {num} es Impar')


num2 = int(input("Ingresa un número para saber si es par o impar: "))
par_impar(num2)

# 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.


def el_mayor(a, b, c):
    if a < b:
        if b < c:
            print('El mayor es: ', c)
        else:
            print('El mayor es: ', b)
    elif a > b:
        if a < c:
            print('El mayor es: ', c)
        else:
            print('El Mayor es:', a)


print('ingrese a continuación tres numeros para saber cual es el mayor')
num3 = int(input("Numero 1: "))
num4 = int(input("Numero 2: "))
num5 = int(input("Numero 3: "))

el_mayor(num3, num4, num5)
