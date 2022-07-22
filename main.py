from gl import *

#Matriz del primer polígono.
p1 = [
    [165, 380], #Primera fila y primera columna. (Primer punto de la primera fila)
    [185, 360], #Segunda fila y primera columna. (Primer punto de la segunda fila)
    [180, 330], #Tercera fila y primera columna. (Punta de la izquierda abajo)
    [207, 345], #Cuarta fila y primera columna. (Punto de en medio abajo)
    [233, 330], #Cuarta fila y segunda columna. (Punta de la derecha abajo)
    [230, 360], #Segunda fila y segunda columna. (Segundo punto de la segunda fila)
    [250, 380], #Primera fila y cuarta columna. (Último punto de la primea fila)
    [220, 385], #Primera fila y tercera columna. (Tercer punto de la primera fila)
    [205, 410], #Punta de hasta arriba de la estrella.
    [193, 383], #Primera fila y segunda columna. (Segundo punto de la primera fila)
]

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

    #Recorriendo la matriz p1.
    for i in range(len(p1)):
        #print(p1[i][0], p1[i][1])
        glVertex(p1[i][0], p1[i][1])


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