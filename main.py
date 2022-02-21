import parametros
import tablero
import CreacionTableros
import Guardado
import math
import random
import os

## Inicio
print("Bienvenid@ a LegoSweeper")
print("Seleccione una opción:\n[1] Crear partida\n[2] Cargar partida\n[3] Ver ranking\n[0] Salir")
opcion = input("Indique su opción: ")
while ord(opcion[0]) < 48 or ord(opcion[0]) > 51 or len(opcion) > 1:
    opcion = input("Indique una opción válida: ")

## Ver ranking
while int(opcion) == 3:
    if not os.path.isfile("puntajes.txt"):
        print("No existen partidas guardadas hasta el momento")
    else:
        puntajes = open("puntajes.txt")
        print("\n ---------------\n")
        print("\n Top 10 Puntajes:\n")
        ranking = []
        for linea in puntajes:
            ranking.append(linea.strip().split(": "))
        ranking.sort(key = lambda x: int(x[1]), reverse = True)
        if int(len(ranking)) > 10:
            for i in range(10, int(len(ranking))):
                ranking.remove(ranking[int(i)])
        place = 1
        for obj in ranking:
            print("  " + str(place) + ".- " + str(obj[0]) + ": " + str(obj[1]))
            place += 1
        print("\n ---------------\n")
    print("Escoja una opción:\n[1] Crear partida\n[2] Cargar partida\n[3] Ver ranking\n[0] Salir")
    opcion = input("Indique su opción: ")
    while ord(opcion[0]) < 48 or ord(opcion[0]) > 51 or len(opcion) > 1:
        opcion = input("Indique una opción válida: ")

## Crear Partida
if int(opcion) == 1:
    username = input("Ingrese un nombre de usuario: ")
    width = input("Ingrese ancho del tablero (min:3 max:15): ")
    while not str.isdigit(width):
        width = input("Ïngrese un número válido (min:3 max:15): ")
    while int(width)<3 or int(width) > 15:
        width = input("Ïngrese un número válido (min:3 max:15): ")
    height = input("Ingrese alto del tablero (min:3 max:15): ")
    while not str.isdigit(height):
        height = input("Ïngrese un número válido (min:3 max:15): ")
    while int(height)<3 or int(height) > 15:
        height = input("Ïngrese un número válido (min:3 max:15): ")
    # Número de Legos (parámetro entregado)
    legos = math.ceil(float(int(width) * int(height) * float(parametros.PROB_LEGO)))
    # Tablero de juego
    height = int(height)
    width = int(width)
    table_juego = CreacionTableros.crear_tablero_juego(width, height)
    tablero.print_tablero(table_juego)
    # Ubicación de legos en tablero
    k = 1
    death = []
    while k <= legos:
        x = random.randint(0,width-1)
        y = random.randint(0,height-1)
        while [x,y] in death:
            x = random.randint(0,width-1)
            y = random.randint(0,height-1)
        death.append([x,y])
        k += 1
    table_completo = CreacionTableros.crear_tablero_completo(width, height, death)
    partida = open(os.path.join('partidas', str(username) + ".txt"), "w")
    Guardado.guardar_base(username, width, height, legos, death, table_completo)

#Cargar Partida
history = []
if int(opcion) == 2:
    death = []
    username = input("Ingrese un nombre de usuario: ")
    while not os.path.isfile(os.path.join('partidas', str(username) + ".txt")):
        username = input("Ingrese nombre de usuario válido: ")
    partida = open(os.path.join('partidas', str(username) + ".txt"), "r")
    username = partida.readline().strip()
    width = int(partida.readline().strip())
    height = int(partida.readline().strip())
    legos = int(partida.readline().strip())
    for i in range(0, int(legos)):
        linea = partida.readline().strip()
        death.append(linea.strip().split(";"))
        death[i][0] = int(death[i][0])
        death[i][1] = int(death[i][1])
    table_completo = []
    for i in range(0,int(height)):
        linea = partida.readline().strip()
        table_completo.append(linea.strip().split(";"))
    history_len = int(partida.readline().strip())
    for i in range(0, int(history_len)):
        linea = partida.readline().strip()
        history.append(linea.strip().split(";"))
        history[i][0] = int(history[i][0])
        history[i][1] = int(history[i][1])
    table_juego = CreacionTableros.crear_tablero_juego(width,height)
    for pos in history:
        xc = int(pos[0])
        yc = int(pos[1])
        table_juego[yc][xc] = table_completo[yc][xc]
    tablero.print_tablero(table_juego)
    opcion = 1

# Juego

if int(opcion) == 0:
    exit()

if int(opcion) == 1:
    print("¡Comienza el juego!\n")
    inp = input("[1] Descubrir una baldosa\n[2] Salir de la partida\n")
    while int(ord(inp)) < 49 or int(ord(inp)) > 50:
        inp = input("[1] Descubrir una baldosa\n[2] Salir de la partida\n")
    choice = []
    if int(inp) == 1:
        choice = input("Escoja una posición escribiendo letra mayúscula y después número: ")
        let = choice[:1]
        nume = choice[1:]
        while str.isdigit(let) or not str.isdigit(nume) \
            or ord(str(let)) > (64+int(width)) or int(nume) > (int(height)-1):
            choice = input("Escoja una posición válida (ej: B2): ")
            let = choice[:1]
            nume = choice[1:]
        xc = int(ord(str(let)) - 65)
        yc = int(nume)
        while [xc, yc] not in death \
        and int(len(history)) < (int(width)*int(height) - int(legos) - 1) and int(inp) == 1:
            while [xc, yc] in history:
                choice = input("¡Esta baldosa ya está descubierta! Escoja una nueva: ")
                let = choice[:1]
                nume = choice[1:]
                xc = int(ord(str(let)) - 65)
                yc = int(nume)
            if [xc, yc] in death:
                puntaje = legos * len(history) * parametros.POND_PUNT
                tablero.print_tablero(table_completo)
                print("¡Ha perdido el juego! Su puntaje: " + str(puntaje))
                print("¿Desea guardar su puntaje?\n[0] No\n[1] Si\n")
                save = input("Indique una opción: ")
                while int(ord(save)) < 48 or int(ord(save)) > 49 or len(save) > 1:
                    save = input("Indique una opción válida: ")
                if int(save) == 0:
                    partida.close()
                    os.remove(os.path.join('partidas',str(username) + ".txt"))
                    print("¡Hasta luego, " + str(username) + "!")
                    exit()
                elif int(save) == 1:
                    if not os.path.isfile("puntajes.txt"):
                        puntajes = open("puntajes.txt", "w")
                        puntajes.write(str(username) + ": " + str(puntaje) + "\n")
                        puntajes.close()
                        partida.close()
                        os.remove(os.path.join('partidas',str(username) + ".txt"))
                        print("¡Hasta luego, " + str(username) + "!")
                        exit()
                    else:
                        puntajes = open("puntajes.txt", "a")
                        puntajes.write(str(username) + ": " + str(puntaje) + "\n")
                        puntajes.close()
                        partida.close()
                        os.remove(os.path.join('partidas',str(username) + ".txt"))
                        print("¡Hasta luego, " + str(username) + "!")
                        exit()
            history.append([xc, yc])
            table_juego[yc][xc] = table_completo[yc][xc]
            tablero.print_tablero(table_juego)
            inp = input("[1] Descubrir una baldosa\n[2] Guardar partida\n[3] Salir de partida\n")
            while int(ord(inp)) < 49 or int(ord(inp)) > 51 or len(inp) > 1:
                inp = input("[1] Descubrir baldosa\n[2] Guardar partida\n[3] Salir de partida\n")
            if int(inp) == 1:
                choice = input("Elija una posición escribiendo letra mayúscula y después número: ")
                let = choice[:1]
                nume = choice[1:]
                while str.isdigit(let) or not str.isdigit(nume) \
                    or ord(str(let)) > (64+width) or int(nume) > (height-1):
                    choice = input("Escoja una posición válida (ej: B2): ")
                    let = choice[:1]
                    nume = choice[1:]
                xc = int(ord(str(let)) - 65)
                yc = int(nume)
            elif int(inp) == 2:
                history_len = len(history)
                Guardado.guardar_base(username, width, height, legos, death, table_completo)
                partida = open(os.path.join('partidas', str(username) + ".txt"), "a")
                partida.write(str(history_len) + "\n")
                for lista in history:
                    partida.write(str(lista[0]) + ";" + str(lista[1]) + "\n")
                print("¡Partida guardada con éxito!")
                inp = input("[1] Descubrir una baldosa\n[2] Salir de la partida\n")
                while int(ord(inp)) < 49 or int(ord(inp)) > 50 or len(inp) > 1:
                    inp = input("[1] Descubrir una baldosa\n[2] Salir de la partida\n")
                if int(inp) == 1:
                    choice = input("Elija una posición escribiendo letra mayúscula y número: ")
                    let = choice[:1]
                    nume = choice[1:]
                    xc = int(ord(str(let)) - 65)
                    yc = int(nume)
                    while str.isdigit(let) or not str.isdigit(nume) \
                        or ord(str(let)) > (64+width) or int(nume) > (height-1):
                        choice = input("Escoja una posición válida (ej: B2): ")
                        let = choice[:1]
                        nume = choice[1:]
                        xc = int(ord(str(let)) - 65)
                        yc = int(nume)
                    while [xc, yc] in history:
                        print([xc, yc], history)
                        choice = input("¡Esta baldosa ya está descubierta! Escoja una nueva: ")
                        let = choice[:1]
                        nume = choice[1:]
                        xc = int(ord(str(let)) - 65)
                        yc = int(nume)
                        while str.isdigit(let) or not str.isdigit(nume) \
                            or ord(str(let)) > (64+width) or int(nume) > (height-1):
                            choice = input("Escoja una posición válida (ej: B2): ")
                            let = choice[:1]
                            nume = choice[1:]
                            xc = int(ord(str(let)) - 65)
                            yc = int(nume)
                    xc = int(ord(str(let)) - 65)
                    yc = int(nume)
                    inp = 1
                elif int(inp) == 2:
                    partida.close()
                    print("¡Hasta luego, " + str(username) + "!")
                    exit()
            elif int(inp) == 3:
                print("[0] Si desea salir sin guardar\n[1] Si desea salir y guardar")
                guardar = input("Indique su opción: ")
                while int(ord(guardar)) < 48 or int(ord(guardar)) > 49 or len(guardar) > 1:
                    guardar = input("Indique una opción válida: ")
                if int(guardar) == 0:
                    partida.close()
                    os.remove(os.path.join('partidas',str(username) + ".txt"))
                    print("¡Hasta luego, " + str(username) + "!")
                    exit()
                elif int(guardar) == 1:
                    Guardado.guardar_base(username, width, height, legos, death, table_completo)
                    partida = open(os.path.join('partidas', str(username) + ".txt"), "a")
                    partida.write(str(len(history)) + "\n")
                    for lista in history:
                        partida.write(str(lista[0]) + ";" + str(lista[1]) + "\n")
                    print("¡Partida guardada con éxito!\n¡Hasta luego!")
                    partida.close()
                    exit()
        if [xc, yc] in death:
            puntaje = legos * len(history) * parametros.POND_PUNT
            tablero.print_tablero(table_completo)
            print("¡Ha perdido el juego! Su puntaje: " + str(puntaje))
            print("¿Desea guardar su puntaje?\n[0] No\n[1] Si\n")
            save = input("Indique una opción: ")
            while int(ord(save)) < 48 or int(ord(save)) > 49 or len(save) > 1:
                save = input("Indique una opción válida: ")
            if int(save) == 0:
                partida.close()
                os.remove(os.path.join('partidas',str(username) + ".txt"))
                print("\n¡Hasta luego, " + str(username) + "!")
                exit()
            elif int(save) == 1:
                if not os.path.isfile("puntajes.txt"):
                    puntajes = open("puntajes.txt", "w")
                    puntajes.write(str(username) + ": " + str(puntaje) + "\n")
                    puntajes.close()
                    partida.close()
                    os.remove(os.path.join('partidas',str(username) + ".txt"))
                    print("\n¡Hasta luego, " + str(username) + "!")
                    exit()
                else:
                    puntajes = open("puntajes.txt", "a")
                    puntajes.write(str(username) + ": " + str(puntaje) + "\n")
                    puntajes.close()
                    partida.close()
                    os.remove(os.path.join('partidas',str(username) + ".txt"))
                    print("¡Hasta luego, " + str(username) + "!")
                    exit()
        elif int(len(history)) >= (width*height - legos - 1):
            tablero.print_tablero(table_completo)
            puntaje = legos * len(history) * parametros.POND_PUNT
            print("\n¡" + str(username) + " ha ganado la partida!\n")
            print("Puntaje final de " + str(username) + ": " + str(puntaje) + "\n")
            print("¿Desea guardar?\n[1] Si\n[0] No\n")
            save = input("Indique su opción: ")
            while int(ord(save)) < 48 or int(ord(save)) > 49 or len(save) > 1:
                save = input("Indique una opción válida: ")
            if int(save) == 0:
                partida.close()
                os.remove(os.path.join('partidas',str(username) + ".txt"))
                print("\n¡Hasta luego, " + str(username) + "!")
                exit()
            if int(save) == 1:
                if not os.path.isfile("puntajes.txt"):
                    puntajes = open("puntajes.txt", "w")
                    puntajes.write(str(username) + ": " + str(puntaje) + "\n")
                    puntajes.close()
                    partida.close()
                else:
                    puntajes = open("puntajes.txt", "a")
                    puntajes.write(str(username) + ": " + str(puntaje) + "\n")
                    puntajes.close()
                    partida.close()
                print("\n¡Partida guardada con éxito!\n¡Hasta luego!")
                exit()
    elif int(inp) == 2:
        print("[0] Si desea salir sin guardar\n[1] Si desea salir y guardar")
        guardar = input("Indique su opción: ")
        while int(ord(guardar)) < 48 or int(ord(guardar)) > 49 or len(guardar) > 1:
            guardar = input("Indique una opción válida: ")
        if int(guardar) == 0:
            partida.close()
            os.remove(os.path.join('partidas',str(username) + ".txt"))
            print("\n¡Hasta luego, " + str(username) + "!")
            exit()
        elif int(guardar) == 1:
            Guardado.guardar_base(username, width, height, legos, death, table_completo)
            partida = open(os.path.join('partidas', str(username) + ".txt"), "a")
            history_len = len(history)
            partida.write(str(history_len) + "\n")
            for lista in history:
                partida.write(str(lista[0]) + ";" + str(lista[1]) + "\n")
            partida.close()
            print("\n¡Partida guardada con éxito!\n¡Hasta luego!")
            exit()