from gl import *


def main():

    glCreateWindow(500, 500) #Creando la ventana.
    glClearColor(0, 0, 0) #Llenando el color de la pantalla.
    glClear() #Llenando el mapa de bits con el color que se le pasa.

    #Se comentó la instancia que está arriba de f.close() para debuggear el glViewPort().

    """
    #Ancho y alto de la pantalla en donde se dibujará el punto.
    ancho = 501
    alto = 501
    
    #Sumarle uno al ancho y al alto.

    #Posición del viewport.
    posx = 200
    posy = 200

    glViewPort(posx, posy, ancho, alto) #Definiendo el área de la imagen sobre la que se va a poder dibujar.
    """

    glColor(0.8, 0.2, 0.1) #Definiendo el color del punto.
    
    #Creando el primer polígono.
    glVertex(165, 380) #Definiendo el punto inicial del punto.
    glVertex(185, 360) 
    glVertex(180, 330)
    glVertex(207, 345)
    glVertex(233, 330)
    glVertex(230, 360)
    glVertex(250, 380)
    glVertex(220, 385)
    glVertex(205, 410)
    glVertex(193, 383) #Punto final del polígono.



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