import random
#laberentio generado aleatoriamente
def generar_Laberinto(filas, columnas):
    maze = [[1 for _ in range(columnas)] for _ in range(filas)]

    def creacion(x, y):
        direcciones = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(direcciones)
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < columnas and 0 <= ny < filas and maze[ny][nx] == 1:
                maze[y + dy // 2][x + dx // 2] = 0
                maze[ny][nx] = 0
                creacion(nx, ny)

    creacion(random.randrange(0, columnas, 2), random.randrange(0, filas, 2))
    return maze

def laberinto(maze):
    for row in maze:
        print(" ".join("X" if cell == 1 else " " for cell in row))

if __name__ == "__main__":
    filas = 6  # Número de filas
    columnas = 6  # Número de columnas
    maze = generar_Laberinto(filas, columnas)
    laberinto(maze)
