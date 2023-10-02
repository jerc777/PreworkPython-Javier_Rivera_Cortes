'''# 1. Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.
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
'''
# 5. Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.

num1 = int(input('Ingrese un numero para que sus digitos sean sumados: '))


# 6. Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.

# 7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.

# 8. Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.

# 9. Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.

# 10. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.

# 11. Crea una función que, dado un número, verifique si un número es primo.

# 12. Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.
