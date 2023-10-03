# 1. Ejercicio: Define una función que tome dos números y retorne su suma.
def sumar_AB(a, b):
    return (print('La suma es:', (a+b)))


a = int(input('ingrese el primer número para sumar:'))
b = int(input('ingrese el segundo número a sumar:'))
sumar_AB(a, b)

# 2. Ejercicio: Define una función que tome un número y retorne su factorial.

def factorial_num(num):
    cont1 = 1
    facto = 1
    while cont1 <= num:
        facto = facto * cont1
        cont1 += 1
    return (print(f'El factorial de {num}, es: ', facto))


num = int(input('ingrese número para conocer su factorial:'))
factorial_num(num)

# 3. Ejercicio: Define una función que tome un número y determine si es primo.

def num_primo(num):
    if num <= 1:
        return (print('Debe colocar un número mayor a 1'))
    elif num == 2:
        return True
    for cont in range(2, int(num**0.5)+1):
        if num % cont == 0:
            return False
    return True


num2 = int(input('Ingrese un numero para saber si es primo: '))
num_primo(num2)
if num_primo(num2):
    print(f'El número {num2}, Si es primo')
else:
    print(f'El número {num2}, no es primo ')

# 4. Ejercicio: Define una función que reciba una lista de números y retorne la sumade ellos.

def suma_list(lista):
    sum = 0
    cont = 0
    for cont in lista:
        # print(cont)
        sum = sum + cont
    print('La suma de los numeros introducidos es', sum)


lista = [40, 25, 15, 10, 6, 2, 2]
suma_list(lista)

# .........Variacion del ejercicio.....(arreglar)........
# si es que la lista se pasa numero a numero por pantalla

def suma_lista(lista):
    sum = 0
    for cont in lista:
        # print(cont)
        sum = sum + int(cont)
    print('La suma de los numeros introducidos es: ', sum)

lista_num = []
while True:
    num = input(
        'Ingrese los numeros de la lista que quiere sumar, y escriba "fin" para finlaizar: ')
    if num == 'fin':
        break
    lista_num.append(num)

suma_lista(lista_num)

# 5. Ejercicio: Define una función que reciba una cadena de texto y retorne lacadena en reversa.

cadena = input('Escriba aqui para obtener lo escrito de manera invertida: ')
cont1 = 1
cont2 = len(cadena) - 1

cadena_invertida = []

while cont1 <= len(cadena):
    cadena_invertida.append(cadena[cont2])
    # print(cadena[cont2])
    cont1 += 1
    cont2 -= 1

print('Lo escrito anteriormente de manera invertida se queda como: ')
print(cadena_invertida)
