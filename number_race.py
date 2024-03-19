import random
import os
import time

#Functions
def loading_dots(duration, interval):
    start_time = time.time()
    print()
    while time.time() - start_time < duration:
        for _ in range(10):
            print(".", end="", flush=True)
            time.sleep(interval)
    print()

def lanzar_dados():
    return random.randint(1, 6)

def jugar(cantidad_jugadores, nivel):
    meta = {1: 20, 2: 30, 3: 50, 4: 100}
    posiciones = [0] * cantidad_jugadores
    pares_consecutivos = [0] * cantidad_jugadores

    

    while True:
        loading_dots(2, 0.2)
        for jugador in range(cantidad_jugadores):
            input(f"::::::::::Turno del jugador {jugador + 1}. :::::::::: \n Presiona Enter para lanzar los dados...")
            dado1 = lanzar_dados()
            dado2 = lanzar_dados()
            loading_dots(2, 0.2)
            print(f"Jugador {jugador + 1} lanzó los dados \n : {dado1} y {dado2}")
            total = dado1 + dado2
            posiciones[jugador] += total
            print(f"El jugador {jugador + 1} \n avanzó {total} posiciones y ahora está en la posición {posiciones[jugador]} \n ")
    
            if dado1 == dado2:
                pares_consecutivos[jugador] += 1
                if pares_consecutivos[jugador] == 3:
                    print(f"¡El jugador {jugador + 1} ha obtenido 3 pares consecutivos y ha ganado!")
                    return
            
            if posiciones[jugador] >= meta[nivel]:
                print(f"::::::::¡FELICIDADES JUGADOR {jugador + 1} HAZ LLEGADO A LA META!:::::::: \n")
                return

def main_menu():
    opt_status = True

    while True:
        os.system('clear')
        print("::::::::::::::::::::::::::::")
        print("::: ¿LISTO PARA EMPEZAR? :::")
        print("[1]. Play")
        print("[4]. Exit")
        
        while opt_status:
            try:
                opt = int(input(".::: presione una opcion: "))
                if opt < 1 or opt > 4:
                    print("::: opcion invalida, intente nuevamente :::")
                else:
                    opt_status = False
            except ValueError:
                print("::: porfavor precione un numero valido :::")
        
        if opt == 1:
            os.system('clear')
            cantidad_jugadores = int(input("Ingrese la cantidad de jugadores (entre 2 y 4): "))
            while not validar_jugadores(cantidad_jugadores):
                cantidad_jugadores = int(input("Ingrese la cantidad de jugadores (entre 2 y 4): "))
            loading_dots(5, 0.5)
            
            os.system('clear')
            print("\nNiveles disponibles:")
            print("1. Nivel básico (Tablero de 20 posiciones)")
            print("2. Nivel intermedio (Tablero de 30 posiciones)")
            print("3. Nivel avanzado (Tablero de 50 posiciones)")
            print("4. Nivel experto (Tablero de 100 posiciones)")
            nivel = int(input("\n Ingrese el nivel de tablero a jugar: "))
            while not validar_nivel(nivel):
                os.system('clear')
                nivel = int(input("\n Ingrese el nivel de tablero a jugar: "))
            
            jugar(cantidad_jugadores, nivel)
            opt_status = True
        elif opt == 4:
            print("Exiting game...")
            break

def validar_jugadores(cantidad_jugadores):
    if cantidad_jugadores < 2 or cantidad_jugadores > 4:
        print("Error: La cantidad de jugadores debe ser de 2 a 4.")
        return False
    return True

def validar_nivel(nivel):
    if nivel not in [1, 2, 3, 4]:
        print("Error: Por favor selecciona un nivel válido.")
        return False
    return True

#Main
os.system('clear')
loading_dots(5, 0.5)
main_menu()






