def Suma():
    numeros = []
    while True:
        entrada = input("Ingrese un número: ")
        print()
        if entrada != "":
            numero = float(entrada)
            numeros.append(numero)
        elif entrada == "":
            sum = 0
            cont = 0
            for cont in numeros:
                sum = sum + cont
            resultado_acumulado = sum
            print("                La suma de los números introducidos es:", sum)
            print()
            break


def Resta(valor):
    # hay que mejorar para que no entren numeros negativos
    while True:
        valor_restante = input(
            "Ingresa el siguiente numero o enter para terminar: ")
        if not valor_restante:
            break
        numero = float(valor_restante)
        valor = valor - numero
    resultado_acumulado = valor
    return print("\n                La resta de los números introducidos es:", valor)


def Multiplicacion(valor):
    while True:
        valor_restante = input(
            "Ingresa el siguiente numero o enter para terminar: ")
        if not valor_restante:
            break
        numero = float(valor_restante)
        valor = valor * numero
    resultado_acumulado = valor
    return print("\n                La multiplicación de los números introducidos es:", valor)


def denom_cero():
    den = 0
    while True:
        if den == 0:
            print(
                "                 Are you insane?, Intenta con cualquier otro numero MENOS ese")
            den = float(input("dime cual: "))
        else:
            return den


def Division(numerador, denominador):
    while True:
        if denominador == 0:
            denominador = denom_cero()
        else:
            resultado = numerador / denominador
            print("\n                La División entre estos números es:", resultado)
            while True:
                seguir = input(
                    "\n    Quieres seguir dividiendo este numero ?.... si/No: ")
                if seguir.lower() == "no":
                    break
                elif seguir.lower() == "si":
                    denominador2 = float(
                        input("\nIngresa el otro denominador: "))
                    if denominador2 == 0:
                        denominador2 = denom_cero()
                    else:
                        resultado2 = resultado / denominador2
                        resultado = resultado2
                        print(
                            "\n                La División entre estos números es:", resultado2)


def Potencias(base, exponente):
    resultado = base ** exponente
    resultado_acumulado = resultado
    return resultado


def Raices(indice, radicando):
    inverso = 1/indice
    resultado = Potencias(radicando, inverso)
    resultado_acumulado = resultado
    return resultado


def dec_to_bin(numero):
    numero_binario = []
    numero_des = numero
    if numero == 0:
        return (print('El numero binario es 0'))
    while numero_des > 0:
        valor_binario = numero_des % 2
        numero_binario.append(valor_binario)
        numero_des = numero_des // 2
    numero_binario.reverse()
    resultado_acumulado = numero_binario
    return numero_binario


def operaciones(n):
    if n == 1:
        print(" Ingrese los valor que quiera sumar, y use enter para finalizar \n")
        Suma()
    elif n == 2:
        print(" A continuación ingrese los valor que quiera Restar \n")
        valor1 = float(input("Ingrese el primer valor: "))
        Resta(valor1)
    elif n == 3:
        print(" A continuación ingrese los valores que quiera Multiplicar \n")
        num = float(input("Ingrese el primer valor: "))
        Multiplicacion(num)
    elif n == 4:
        print(" A continuación ingrese los valores que quiera dividir \n")
        numerador = float(input("Ingrese el numerador: "))
        denominador = float(input("Ingresa el denominador: "))
        Division(numerador, denominador)
    elif n == 5:
        print(" A continuación ingrese la Base y luego el Exponente de la potencia que desea calcular \n")
        base = float(input("Base: "))
        exponente = float(input("Exponente: "))
        print("\n                el resultado es: ", Potencias(base, exponente))
    elif n == 6:
        print(" A continuación ingrese el índice y el radicando de la Raìz que desea calcular \n")
        indice = int(input("Índice: "))
        radicando = int(input("Radicando: "))
        print("\n                el resultado es: ", Raices(indice, radicando))
    elif n == 7:
        print(" A continuación ingrese el numero en base decimal que quiera convertir a binario \n")
        numero = int(input("Numero en base decimal: "))
        print(
            f"\n                el numero {numero} en binario es: ", dec_to_bin(numero))


def Calculadora():
    print()
    print("...!!!  BIENVENIDO A LA CALCULADORA BASICA  !!!...\n")
    print(" las opciones son las siguiente: ")
    resultado_acumulado = 0
    while True:
        print(f"\n [1] Suma \n [2] Resta \n [3] Multiplicación \n [4] División \n [5] Potencias \n [6] Raices \n [7] Cambio de Decimal a binario \n [8] Salir \n")
        eleccion = int(input(" Diga su elección: "))
        print()
        if 1 <= eleccion < 8:
            operaciones(eleccion)
        elif eleccion == 8:
            print("                Ok, Hasta luego...\n ")
            break
        else:
            print("                   [ Debe ingresar una opcion válida ] ")


if __name__ == "__main__":
    Calculadora()
