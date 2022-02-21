# Se crea tablero sobre el cual se desarrollará el juego...

def crear_tablero_juego(N, M):
    table_juego = []
    i = 0
    j = 0
    for i in range(0, int(M)):
        l = []
        for j in range(0, int(N)):
            l.append(str(' '))
            j += 1
        table_juego.append(l)
        i += 1
    return table_juego



# Se crea tablero "solución" que otorgará los números y legos a las posiciones del tablero de juego

def crear_tablero_completo(N, M, pos_legos):
    table_completo = []
    for i in range(0, int(M)):
        l = []
        for j in range(0, int(N)):
            l.append(str(' '))
        table_completo.append(l)
    for [x,y] in pos_legos:
        table_completo[y][x] = 'L'
    for i in range(0, int(M)):
        for j in range(0, int(N)):
            count = 0
            if table_completo[i][j] != 'L':
                if i == 0 and j == 0:
                    if table_completo[i+1][j+1] == 'L':
                        count += 1
                    if table_completo[i][j+1] == 'L':
                        count += 1
                    if table_completo[i+1][j] == 'L':
                        count += 1
                    table_completo[i][j] = str(count)
                if i == M-1 and j == 0:
                    if table_completo[i-1][j] == 'L':
                        count += 1
                    if table_completo[i][j+1] == 'L':
                        count += 1
                    if table_completo[i-1][j+1] == 'L':
                        count += 1
                    table_completo[i][j] = str(count)
                if i == 0 and j == N-1:
                    if table_completo[i+1][j] == 'L':
                        count += 1
                    if table_completo[i][j-1] == 'L':
                        count += 1
                    if table_completo[i+1][j-1] == 'L':
                        count += 1
                    table_completo[i][j] = str(count)
                if i == M-1 and j == N-1:
                    if table_completo[i-1][j] == 'L':
                        count += 1
                    if table_completo[i][j-1] == 'L':
                        count += 1
                    if table_completo[i-1][j-1] == 'L':
                        count += 1
                    table_completo[i][j] = str(count)
                if i == 0 and j>0 and j<N-1:
                    if table_completo[i][j-1] == 'L':
                        count += 1
                    if table_completo[i+1][j-1] == 'L':
                        count += 1
                    if table_completo[i+1][j] == 'L':
                        count += 1
                    if table_completo[i+1][j+1] == 'L':
                        count += 1
                    if table_completo[i][j+1] == 'L':
                        count += 1
                    table_completo[i][j] = str(count)
                if j == 0 and i>0 and i<M-1:
                    if table_completo[i][j+1] == 'L':
                        count += 1
                    if table_completo[i+1][j+1] == 'L':
                        count += 1
                    if table_completo[i-1][j] == 'L':
                        count += 1
                    if table_completo[i-1][j+1] == 'L':
                        count += 1
                    if table_completo[i+1][j] == 'L':
                        count += 1
                    table_completo[i][j] = str(count)
                if i == M-1 and j>0 and j<N-1:
                    if table_completo[i][j-1] == 'L':
                        count += 1
                    if table_completo[i-1][j-1] == 'L':
                        count += 1
                    if table_completo[i-1][j] == 'L':
                        count += 1
                    if table_completo[i-1][j+1] == 'L':
                        count += 1
                    if table_completo[i][j+1] == 'L':
                        count += 1
                    table_completo[i][j] = str(count)
                if j == N-1 and i>0 and i<M-1:
                    if table_completo[i][j-1] == 'L':
                        count += 1
                    if table_completo[i-1][j-1] == 'L':
                        count += 1
                    if table_completo[i-1][j] == 'L':
                        count += 1
                    if table_completo[i+1][j-1] == 'L':
                        count += 1
                    if table_completo[i+1][j] == 'L':
                        count += 1
                    table_completo[i][j] = str(count)
                if i>0 and i<M-1 and j>0 and j<N-1:
                    if table_completo[i][j-1] == 'L':
                        count += 1
                    if table_completo[i-1][j-1] == 'L':
                        count += 1
                    if table_completo[i-1][j] == 'L':
                        count += 1
                    if table_completo[i+1][j-1] == 'L':
                        count += 1
                    if table_completo[i+1][j] == 'L':
                        count += 1
                    if table_completo[i-1][j+1] == 'L':
                        count += 1
                    if table_completo[i][j+1] == 'L':
                        count += 1
                    if table_completo[i+1][j+1] == 'L':
                        count += 1
                    table_completo[i][j] = str(count)
    return table_completo