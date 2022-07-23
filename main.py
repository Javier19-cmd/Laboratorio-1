from gl import *

#Matriz del primer polígono.

m = [
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

# m =[
#     [165, 380, 0, 0, 0],
#     [0, 0, 0, 185, 360, 0, 0],
#     [0, 0, 180, 330, 0, 0, 0],
#     [0, 207, 345, 0, 0, 0, 0],
#     [0, 0, 233, 330, 0, 0, 0],
#     [0, 0, 230, 360, 0, 0, 0],
#     [0, 0, 0, 250, 380, 0, 0],
#     [0, 220, 385, 0, 0, 0, 0],
#     [0, 0, 0, 205, 410, 0, 0],
#     [193, 383, 0, 0, 0, 0, 0],
#     ] #Matriz de puntos.

# pl1 = [
#     [165, 380, 0, 0, 0, 0, 0, 0], #Primera fila y primera columna. (Primer punto de la primera fila)
#     [185, 360, 0, 0, 0, 0, 0, 0], #Segunda fila y primera columna. (Primer punto de la segunda fila)
#     [180, 330, 0, 0, 0, 0, 0, 0], #Cuarta fila y primera columna. (Punta de la izquierda abajo)
#     [0, 0, 0, 207, 345, 0, 0, 0], #Tercera fila y primera columna. (Punto de en medio abajo)
#     [0, 0, 0, 0, 0, 0, 233, 330], #Cuarta fila y segunda columna. (Punta de la derecha abajo)
#     [0, 0, 0 , 0, 0, 0, 230, 360], #Segunda fila y segunda columna. (Segundo punto de la segunda fila)
#     [0, 0, 0 , 0, 0, 0, 250, 380], #Primera fila y cuarta columna. (Último punto de la primea fila)
#     [0, 0, 0, 0, 220, 385, 0, 0], #Primera fila y tercera columna. (Tercer punto de la primera fila)
#     [0, 0, 0, 205, 410, 0, 0, 0], #Punta de hasta arriba de la estrella.
#     [0, 0, 193, 383, 0, 0, 0, 0], #Primera fila y segunda columna. (Segundo punto de la primera fila)
# ]

def main():

    glCreateWindow(500, 500) #Creando la ventana.
    glClearColor(255, 255, 255) #Llenando el color de la pantalla.
    glClear() #Llenando el mapa de bits con el color que se le pasa.

    #Se comentó la instancia que está arriba de f.close() para debuggear el glViewPort().

    glColor(204, 0, 0) #Definiendo el color del punto.
    
    #Creando el primer polígono.
    # glVertex(165, 380) #Definiendo el punto inicial del punto.
    # glVertex(185, 360) 
    # glVertex(180, 330)
    # glVertex(207, 345)
    # glVertex(233, 330)
    # glVertex(230, 360)
    # glVertex(250, 380)
    # glVertex(220, 385)
    # glVertex(205, 410)
    # glVertex(193, 383) #Punto final del polígono.

    # #Recorrer la matriz de puntos.
    # for i in range(len(m)):
    #     for j in range(len(m[i])):
    #         #print("m[i][j] = ", m[i][j])
    #         if m[i][j] != 0:
    #             #print("Hola")
    #             #print(m[i][j - 1], m[i - 1][j])	
    #             #print("Después del if: ", m[i][j], m[i][j + 1])
    #             glVertex(m[i][j], m[i][j + 1])

    #Recorriendo la matriz p1.
    for i in range(len(m)):
        #print(p1[i][0], p1[i][1])
        glVertex(m[i][0], m[i][1])

    

    #Creando el segundo polígono.
    # glVertex(321, 335)
    # glVertex(288, 286)
    # glVertex(339, 251)
    # glVertex(374, 302)



    #Creando el tercer polígono.
    # glVertex(377, 249)
    # glVertex(411, 197)
    # glVertex(436, 249)

    glFinish() #Escribiendo la ventana.

main()