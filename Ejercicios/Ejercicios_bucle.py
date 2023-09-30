
# 1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista:
    print(numero)

# 2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
cont = 1
while cont <= 20:
    if cont % 2 == 0:
        print(cont)
    cont += 1


# 3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
cont2 = 1
sum = 0
while cont2 <= 100:
    sum = sum + cont2
    if cont2 == 100:
        print(sum)
    cont2 += 1
