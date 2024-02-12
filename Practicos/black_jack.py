import random

# constantes
pintas = ("Corazones", "Diamantes", "Espadas", "Treboles")
valor_carta_escrito = ("As", "Dos", "Tres", "Cuatro", "Cinco","Seis", "Siete", "Ocho", "Nueve", "Diez", "J", "Q", "K")
valor_carta_numero = {"As": 11, "Dos": 2, "Tres": 3, "Cuatro": 4, "Cinco": 5,"Seis": 6, "Siete": 7, "Ocho": 8, "Nueve": 9, "Diez": 10, "J": 10, "Q": 10, "K": 10}


class Fichas:
    def __init__(self,fichas_total):
        self.fichas_total = fichas_total
        self.apuesta = 0

    def ganar_apuesta(self):
        self.fichas_total += self.apuesta
        print(self.fichas_total)

    def perder_apuesta(self):
        self.fichas_total -= self.apuesta

    def __str__(self):
        return 'Tienes ' + str(self.fichas_total) + ' fichas restantes'
    
# Como se actualizan las fichas usando estas caracteristicas de la calse ficha ??

class Carta:
    def __init__(self, pintas, valor_carta_numero):
        self.pintas = pintas
        self.valor_carta_numero = valor_carta_numero
    def __str__(self):
        return str(self.valor_carta_numero) + ' de ' + self.pintas

class Baraja:
    def __init__(self):
        self.baraja = []
        for pinta in pintas:
            for numero in valor_carta_numero:
                self.baraja.append(Carta(pintas, valor_carta_numero))

    def barajar(self):
        random.shuffle(self.baraja)

    def quitar_una_carta(self):
        return self.baraja.pop()

    def __str__(self):
        resultado = ''
        for carta in self.baraja:
            resultado += '\n' + carta.__str__()
        return 'Mi baraja tiene: ' + resultado

fichas_total = int(input("Con cuantas fichas quiere empezar a jugar: "))
fichas_jugador = Fichas(fichas_total)
print(fichas_jugador)
cartas = Baraja()
print(cartas)



"""
def blackjack():
    fichas_inicial = int(input("Con cuantas fichas quiere empezar a jugar"))
    fichas_jugador = Fichas(fichas_inicial)
    while True:
        jugando = True
        print("Bienvenido al Casino Black Jack")
        mi_baraja= Baraja()
        mi_baraja.barajar()

        mano_jugador = Mano()

        mano_crupier = Mano()

        mano_jugador.robar(mi_baraja.quitar_una_carta())
        mano_jugador.robar(mi_baraja.quitar_una_carta())


        mano_crupier.robar(mi_baraja.quitar_una_carta())
        mano_crupier.robar(mi_baraja.quitar_una_carta())

        hacer_apuesta(fichas_jugador)


        while jugando:

            enseñar_algunas(mano_jugador, mano_crupier)

            jugando = quieres_otra_carta(mi_baraja, mano_jugador, mano_crupier, jugando)

            if mano_jugador.suma > 21:
                if mano_jugador.numero_ases > 0:
                    mano_jugador.ajustar_ases()
                else:
                    jugando = False
        
        if mano_jugador.suma <= 21:
            while mano_crupier.suma <= 17:
                repartir_carta(mano_crupier, mi_baraja)
                mano_crupier.ajustar_ases()
        
            if mano_jugador.suma > mano_crupier.suma:
                print("Has ganado!\n")
                fichas_jugador.cantidad_total += fichas_jugador.apuesta
            
            else:
                if mano_crupier.suma <= 21:
                    print("Has perdido!\n")
                    fichas_jugador.cantidad_total -= fichas_jugador.apuesta
                elif mano_crupier.suma == mano_jugador.suma:
                    print("Empate!\n")
                else:
                    print("Has ganado!\n")
                    fichas_jugador.cantidad_total += fichas_jugador.apuesta

        else:
            print("Has perdido!")
            fichas_jugador.cantidad_total -= fichas_jugador.apuesta

        enseñar_todas(mano_jugador, mano_crupier)

        print("\nLa cantidad de fichas del jugador es de: ", fichas_jugador.cantidad_total)

        nueva_partida = input("Quieres jugar otra partida?(S/N): ")

        if nueva_partida[0].lower() == 's':
            jugando=True
            continue
        else:
            print('Gracias por jugar!!')
            break


blackjack()

"""