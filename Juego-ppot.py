nombre1 = input ("¿como se llama el jugador 1?")
nombre2 = input ("¿como se llama el jugador 2?")

jugador1 = input ("hola jugador uno! Â¿que elijes? ¿Piedra, papel, tijera?: ")
jugador2 = input ("hola jugador dos! Â¿que elijes? ¿Piedra, papel, tijera?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print ("ha sido un empato")
elif (condicion1  or condicion2 or condicion3):
    print ("ha ganado:", nombre1)
else: 
    print("haganado:", nombre2)
