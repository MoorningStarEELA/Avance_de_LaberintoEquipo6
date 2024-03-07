def creacion_Laberinto(corredores):
    for filas in corredores:
        print("".join(str(cell)for cell in filas))

laberinto = [
    [1 ,1 ,1 ,0 ,0 ,0 ], #1  = camino 
    [0 ,1 ,0 ,1 ,0 ,0 ],  #0  = pared 
    [0 ,1 ,1 ,1 ,1 ,0 ],
    [1 ,1 ,0 ,0 ,0 ,0 ],
    [1 ,0 ,0 ,0 ,0 ,0 ],
    [1 ,1 ,1 ,1 ,1 ,1 ],
]

print("Laberinto Vs1 .1 : ")

creacion_Laberinto(laberinto)
