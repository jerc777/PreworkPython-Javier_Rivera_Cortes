
def llenar_tablero(espacio):
    for i in range(len(espacio)):
        for j in range(len(espacio[i])):
            if j == 1 or j == 3:
                espacio[i][j] = ' | '
            elif j == 0:
                espacio[i][j] = opciones[i][0]
            elif j == 2:
                espacio[i][j] = opciones[i][1]
            elif j == 4:
                espacio[i][j] = opciones[i][2]


def imprimir_tablero():
    print()
    for i_fila, fila in enumerate(tablero):
        i = 0
        while i < 5:
            print(fila[i], end='')
            i += 1
        print()
        if i_fila < 2:
            print('-'*9)
    print()


def turno(a):
    if a < 10:
        if a % 2 == 0:
            print('Turno de : ', p2)
        else:
            print('Turno de : ', p1)
    else:
        print('Tablero lleno')


def llenado_opciones(x, y, a):
    if a % 2 == 0:
        opciones[x-1][y-1] = 'O'
    else:
        opciones[x-1][y-1] = 'X'


def revision_filas(opcion):
    if opcion[0][0] == opcion[0][1] == opcion[0][2] != ' ' or opcion[1][0] == opcion[1][1] == opcion[1][2] != ' ' or opcion[2][0] == opcion[2][1] == opcion[2][2] != ' ':
        return (True)
    else:
        return (False)


def revision_columna(opcion):
    if opcion[0][0] == opcion[1][0] == opcion[2][0] != ' ' or opcion[0][1] == opcion[1][1] == opcion[2][1] != ' ' or opcion[0][2] == opcion[1][2] == opcion[2][2] != ' ':
        return (True)
    else:
        return (False)


def revision_diagonal(opcion):
    if (opcion[0][0] == opcion[1][1] == opcion[2][2] or opcion[2][0] == opcion[1][1] == opcion[0][2]) and opcion[1][1] != ' ':
        return True
    else:
        return False


def comprobacion(opciones):
    # hay que hacer con if que mientras sea diferente a espacio vacío
    if revision_columna(opciones) or revision_diagonal(opciones) or revision_filas(opciones):
        return True
    return False


def ganador(a):
    if a % 2 == 0:
        print('El ganador es: ', p2)
    else:
        print('El ganador es: ', p1)


def juego():
    imprimir_tablero()
    a = 1
    while a < 10:
        turno(a)
        print('Indique su elección: ')
        coordenada_x = int(input("Coordenada x: "))
        coordenada_y = int(input("Coordenada y: "))
        if opciones[coordenada_x-1][coordenada_y-1] == ' ':
            llenado_opciones(coordenada_x, coordenada_y, a)
            llenar_tablero(tablero)
            imprimir_tablero()
            if comprobacion(opciones):
                ganador(a)
                break
            a += 1
        else:
            print()
            print('Sitio Ocupado')
            print()


# Crear un tablero vacío
tablero = [[" " for _ in range(5)] for _ in range(3)]
# Crear matriz de opciones
opciones = [[" " for _ in range(3)] for _ in range(3)]

# Llenar el tablero
llenar_tablero(tablero)

# inicio
print()
print('Bienvenido al tres en raya\n')
print('Indique el nombre de los jugadores\n')
p1 = input('Jugador 1 (X): ')
p2 = input('Jugador 2 (O): ')
print()
print('las instrucciones son las siguiente:\n1) Solo debe colocar una X y una O según sea el caso\n2) Para poner su opción deberá indicar las coordenadas, por ejemplo\n   el primer cuadrante tiene coordenada (x,y) igual a (1,1)\n')

juego()
