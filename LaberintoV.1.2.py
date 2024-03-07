def creacion_Laberinto(corredores):
    for fila in corredores:
        print("".join(str(cell) for cell in fila))

def encontrar_salida(maze, inicio, fin):
    filas = len(maze)
    columnas = len(maze[0])
    visitado = [[False] * columnas for _ in range(filas)]

    def recorrido(x, y):
        if x == fin[0] and y == fin[1]:
            return True
        if maze[y][x] == 0 or visitado[y][x]:
            return False

        visitado[y][x] = True

        # Movimientos posibles (izquierda, derecha, arriba, abajo)
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < columnas and 0 <= ny < filas:
                if recorrido(nx, ny):
                    return True

        return False

    return recorrido(inicio[0], inicio[1])

if __name__ == "__main__":
    laberinto = [
        [1, 1, 1, 0, 0, 0], 
        [0, 1, 0, 1, 0, 0], 
        [0, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
    ]

    print("Laberinto Vs1 .1 : ")
    creacion_Laberinto(laberinto)

    inicio = (0, 0)  # Posición de inicio
    fin = (len(laberinto)-1, len(laberinto[0])-1)  # Posición de fin

    if encontrar_salida(laberinto, inicio, fin):
        print("Se encontró una salida en el laberinto.")
    else:
        print("No se encontró una salida en el laberinto.")
