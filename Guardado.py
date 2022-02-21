import os 

def guardar_base(username, N, M, L, pos_legos, tablero_completo):
    partida = open(os.path.join('partidas', str(username) + ".txt"), "w")
    partida.write(str(username) + "\n")
    partida.write(str(N) + "\n")
    partida.write(str(M) + "\n")
    partida.write(str(L) + "\n")
    for lista in pos_legos:
        partida.write(str(lista[0]) + ";" + str(lista[1]) + "\n")
    for pos in tablero_completo:
        for i in range(0,N):
            if int(i) == N-1:
                partida.write(str(pos[i]))
            else:
                partida.write(str(pos[i]) + ";")
        partida.write("\n")