def operaciones(n):
        if n == 1: print(suma())
        elif n  == 2: 
        elif n  == 3:
        elif n  == 4:
        elif n  == 5:
        elif n  == 6:
        elif n  == 7:

def Calculadora():
    print()
    print("...!!!  BIENVENIDO A LA CALCULADORA BASICA  !!!...\n")
    print(" las opciones son las siguiente: \n")
    while True:
        print(f" [1] Suma \n [2] Resta \n [3] Multiplicación \n [4] División \n [5] Potencias \n [6] Raices \n [7] Cambio de Decimal a binario \n [8] Salir \n")
        eleccion = input("Diga su elección: " )
        if eleccion != range(1,7):
            print("Debe ingresar una opcion válida ")
        elif eleccion == 8:
            print(" Ok, Hasta luego ")
            break
        else:
            




Calculadora()
