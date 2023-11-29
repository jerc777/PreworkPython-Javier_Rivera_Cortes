def turno(a):
    jugadores = [p1, p2]
    jugador_actual = jugadores[a // 2]
    print('Turno de:', jugador_actual)
    return (a+1)


a = 6
print('Indique el nombre de los jugadores\n')
p1 = input('Jugador 1 (X): ')
p2 = input('Jugador 2 (O): ')
turno(a)
