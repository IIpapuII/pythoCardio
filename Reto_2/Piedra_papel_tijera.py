import os


def menaje_bienvenidad():
    
    print("#################################################")
    print("#  Bienvenido al juego de piedra papel o tigera #")
    print("#################################################")
    print("")
    print("")
    dato = input("Presiona enter para continuar o N para salir: ")
    if(dato == "N"):
        valor = False
    else:
        valor = True
    return valor


def limpiar_screem():
    os.system("cls")


def jugadores_Entradas():
    jugador_uno = str(input("Ingrese piedra papel o tigera: "))
    jugador_dos = str(input("Ingrese piedra, papel o tigera: "))

    return jugador_uno, jugador_dos


def Operaciones():
    uno, dos = jugadores_Entradas()
    if (uno == dos):
        gandor = "empate"
    elif((uno == "piedra") and (dos == "Tigera")):
        print("Ganador jugador uno")
        gandor = "uno"
    else:
        print("salidad")
    return gandor


def main():
    contador1 = 0
    contador2 = 0
    dato = menaje_bienvenidad()
    while(dato == True):
        if(dato == False):
            print("juego terminado")
        else:
            ganador = Operaciones()
            if (ganador == "uno"):
                contador1 = contador1 + 1
                continue
            elif(ganador == "empate"):
                print("jugada igual")
                ganador = Operaciones()
                continue
            elif(ganador == "dos"):
                contador2 = contador2 + 1
                continue
        
        if(contador2<=3 or contador1 <=3):
           if(contador2 < contador1):
                print("ganando jugador uno ")
           else:
            if(contador1 < contador2):
                print("ganando el jugador dos")
        else:
            dato = False


if __name__ == "__main__":
    main()
