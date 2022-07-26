from gl import *

#Matriz del primer polígono.

figura1 = [
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

# figura11 =[
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

# llenado1 = [
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

#Matriz del segundo polígono.
figura2 = [
    [321, 335],
    [288, 286],
    [339, 251],
    [374, 302]
]


#Matriz del tercer polígono.
figura3 = [
    [377, 249],
    [411, 197],
    [436, 249]
]

#Matriz del cuarto polígono.
figura4 = [
    [413, 177],
    [448, 159],
    [502, 88],
    [553, 53],
    [535, 36],
    [676, 37],
    [660, 53],
    [750, 145],
    [761, 179],
    [672, 192],
    [659, 214],
    [615, 214],
    [632, 230],
    [580, 230],
    [597, 215],
    [552, 214],
    [517, 144],
    [466, 180]

]

#Matriz del quinto polígono.
figura5 = [
    [682, 175],
    [708, 120],
    [735, 148],
    [739, 170]
]


def main():

    colorP = color(0,0,0)
    colorP2 = color(255,100,0)
    colorP3 = color(92, 150, 25)

    glCreateWindow(800, 800) #Creando la ventana.
    glClearColor(0, 0, 0) #Llenando el color de la pantalla.
    glClear() #Llenando el mapa de bits con el color que se le pasa.
    #Se comentó la instancia que está arriba de f.close() para debuggear el glViewPort().

    glColor(255, 100, 0) #Definiendo el color del punto.
    
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

    # #Recorriendo la matriz figura1.
    for i in range(len(figura1)):
        #Aquí se ponen los puntos en el mapa de bits.
        #print(p1[i][0], p1[i][1])
        glVertex(figura1[i][0], figura1[i][1])

    #Haciendo línea entre los puntos.
    line(165, 380, 185, 360) #Inicio de la figura.
    line(185, 360, 180, 330)
    line(180, 330, 207, 345)
    line(207, 345, 233, 330)
    line(233, 330, 230, 360)
    line(230, 360, 250, 380)
    line(250, 380, 220, 385)
    line(220, 385, 205, 410)
    line(205, 410, 193, 383)
    line(193, 383, 165, 380) #Final de la figura.

    #Llamar a la función que llena la figura.
    flood(220, 350, colorP, colorP2)
    
    #Creando el segundo polígono.

    # #Recorriendo la matriz figura2.
    for i in range(len(figura2)):
        #Aquí se ponen los puntos en el mapa de bits.
        #print(p1[i][0], p1[i][1])
        glVertex(figura2[i][0], figura2[i][1])

    #Uniendo los puntos.
    line(321, 335, 288, 286) #Inicio de la figura.
    line(288, 286, 339, 251)
    line(339, 251, 374, 302)
    line(374, 302, 321, 335) #Final de la figura.

    #glVertex(325, 300)

    flood(325, 300, colorP, colorP2)

    #Creando el tercer polígono.
    # #Recorriendo la matriz figura3.
    for i in range(len(figura3)):
        #Aquí se ponen los puntos en el mapa de bits.
        #print(p1[i][0], p1[i][1])
        glVertex(figura3[i][0], figura3[i][1])

    #Uniendo los puntos del tercer polígono.
    line(377, 249, 411, 197) #Inicio de la figura.
    line(411, 197, 436, 249)
    line(436, 249, 377, 249) #Final de la figura.

    #glVertex(410, 220)
    flood(410, 220, colorP, colorP2)

    # #Recorriendo la matriz figura3.
    for i in range(len(figura4)):
        #Aquí se ponen los puntos en el mapa de bits.
        #print(p1[i][0], p1[i][1])
        glVertex(figura4[i][0], figura4[i][1])

    line(413, 177, 448, 159) #Inicio de la figura.
    line(448, 159, 502, 88)
    line(502, 88, 553, 53)
    line(553, 53, 535, 36)
    line(535, 36, 676, 37)
    line(676, 37, 660, 53)
    line(660, 53, 750, 145)
    line(750, 145, 761, 179)
    line(761, 179, 672, 192)
    line(672, 192, 659, 214)
    line(659, 214, 615, 214)
    line(615, 214, 632, 230)
    line(632, 230, 580, 230)
    line(580, 230, 597, 215)
    line(597, 215, 552, 214)
    line(552, 214, 517, 144)
    line(517, 144, 466, 180)
    line(466, 180, 413, 177) #Final de la figura.

    #glVertex(540, 100)
    #glVertex(493, 100)
    #line(707, 54, 400, 54)

    #glVertex(600, 80)
    #flood(600, 80, colorP, colorP2)
    #flood(592, 190, colorP, colorP3)

    #Creando el cuarto polígono.
    # #Recorriendo la matriz figura3.
    for i in range(len(figura5)):
        #Aquí se ponen los puntos en el mapa de bits.
        #print(p1[i][0], p1[i][1])
        glVertex(figura5[i][0], figura5[i][1])
    
    line(682, 175, 708, 120) #Inicio de la figura.
    line(708, 120, 735, 148)
    line(735, 148, 739, 170)
    line(739, 170, 682, 175) #Final de la figura.

    #glVertex(720, 160)
    flood(720, 160, colorP, colorP3)

    glFinish() #Escribiendo la ventana.

main()