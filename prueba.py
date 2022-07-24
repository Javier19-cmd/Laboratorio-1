"""
1. Flood fill: https://python.plainenglish.io/a-python-example-of-the-flood-fill-algorithm-bced7f96f569
"""

import random

me = [
    [165, 380],
    [185, 360],
    [180, 330],
    [207, 345],
    [233, 330],
    [230, 360],
    [250, 380],
    [220, 385],
    [205, 410],
    [193, 383],
]

m =[
    [0, 0, 165, 300, 0, 0, 0],
	[0, 0, 0, 185, 360, 0, 0],
	[0, 0, 180, 330, 0, 0, 0],
	[0, 207, 345, 0, 0, 0, 0],
	[0, 0, 233, 330, 0, 0, 0],
	[0, 0, 230, 360, 0, 0, 0],
	[0, 0, 0, 250, 380, 0, 0],
	[0, 220, 385, 0, 0, 0, 0],
	[0, 0, 0, 205, 410, 0, 0],
	[193, 383, 0, 0, 0, 0, 0],
	] #Matriz de puntos.

def print_matrix(m):
    #En este método se va a imprimir la matriz.
    for y in range(len(m)): 
        for x in range(len(m[0])):
            print(m[y][x], end=" ") #Valor dado por la columna y la fila.

            if x == len(m[0]) - 1:
                #Se imprime el salto de línea.
                print('\n')

def flood_fill(x, y, old_color, new_color):
    #En este método se va a necesitar el  x y el y del punto de inicio, el valor antiguo y el nuevo.

    #El flood fill tiene cuatro partes.
    #Primero, se va a verificar que x y y no sean inválidos.
    if x < 0 or x >= len(m[0]) or y < 0 or y >= len(m):
        return

    #Segundo, se va a verificar que el valor del punto de inicio sea igual al valor antiguo.
    if m[y][x] != old_color:
        return
    
    #Tercero, se va a cambiar el valor del punto de inicio por el nuevo.
    m[y][x] = new_color

    #Cuarto, se van a llenar las posiciones adyacentes.
    flood_fill(x + 1, y, old_color, new_color)
    flood_fill(x - 1, y, old_color, new_color)
    flood_fill(x, y + 1, old_color, new_color)
    flood_fill(x, y - 1, old_color, new_color)

print_matrix(m) #Se imprime la matriz al inicio.
flood_fill(0, 0, 0, 204) #Se llena la matriz.
print("Haciendo el flood fill con '204'...")
print_matrix(m) #Se imprime la matriz al final, luego del flood fill.