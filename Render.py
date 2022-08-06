from utilidades import *
import random
import sys

"""
1. Modificar la recursión de Python:
   https://www.geeksforgeeks.org/python-handling-recursion-limit/#:~:text=When%20you%20execute%20a%20recursive,on%20large%20inputs.
2. Flood fill: 
    http://inventwithpython.com/blog/2011/08/11/recursion-explained-with-the-flood-fill-algorithm-and-zombies-and-cats/
"""

sys.setrecursionlimit(10**9)

#Variables globales.

#Ancho y alto de la pantalla.
anchoP, altoP = 0, 0

#Color del framebuffer.
colorP = 0


#Posiciones de los puntos.
equis, ye = 0, 0

#Prueba del punto.
colorA = 0
#print("Color del punto", colorA)

colorN = color(30, 50, 80)

#Propiedades del viewport.

#Color del viewport.
colorV = 0
#print("Color del viewport", colorV)

#Posición en x, y del viewport.
Posx, Posy = 0, 0

#Ancho y alto del viewport.
Ancho, Alto = 0, 0

#Lista temporal para el viewport.

lista = []

#Framebuffer de la pantalla.
framebuffer = []

#Este método recibe el color del framebuffer.
def recibirColorFondo(color):
    #En este método se setea el color del framebuffer.
    global colorP #Instanciando la variable global del color de la pantalla.

    #Llenando el framebuffer.
    colorP = color


#Método que renderiza el archivo.
def DimensionesPantalla(width, height):
    #En este método se setea el ancho y alto de la pantalla.
    global anchoP, altoP #Instanciando las variables globales del ancho y alto de la pantalla.

    #Llenando las variables globales.
    anchoP = width
    altoP = height

#Método que escribe el framebuffer.
def Framebuffer():
    #En este método se escribe el framebuffer.
    global framebuffer

    #print(colorP)

    #print(colorP)


    #Llenando de bits el framebuffer.
    framebuffer = [
        [colorP for x in range(anchoP)]
        for y in range(altoP)
    ]

#Seteando el color del punto.
def colorPunto(color):
    #En este método se setea el color del punto.
    global colorA #Instanciando la variable global del color del punto.

    #Llenando la variable global.
    colorA = color
    #print("Color del punto", colorA)

def flood_fill(x, y, old, new):
    #Se necesita la posición x y y inicial, el valor del color antiguo y el nuevo color.

    # assume surface is a 2D image and surface[x][y] is the color at x, y.

    theStack = [(x, y)] # stack of pixels to check

    while len(theStack) > 0: #Verificar si la pila está vacía.
        x, y = theStack.pop() #Sacar el último elemento de la pila.

        if framebuffer[x][y] != old: #Verificar si el color es diferente al antiguo.
            continue

        framebuffer[x][y] = new #Poner el nuevo color.

        #Agregando los puntos vecinos a la pila.
        theStack.append((x + 1, y))
        theStack.append((x - 1, y))
        theStack.append((x, y + 1))
        theStack.append((x, y - 1))


def Vertex(x, y):
    #En este método se dibuja un punto en el viewport.
    global equis, ye #Instanciando las variables globales de las posiciones del punto.

    #Llenando las variables globales.
    equis = x
    ye = y

    #print(equis, ye)

    #Colocar el punto en el viewport.
    framebuffer[equis][ye] = colorA
    #print("Color del punto", colorA)


#Método que escribe el archivo bmp.
def write():
        
        #Se abre el archivo con la forma de bw.
        f = open("Lab1.bmp", "bw")

        #Se escribe el encabezado del archivo.

        #Haciendo el pixel header.
        f.write(char('B'))
        f.write(char('M'))
        #Escribiendo el tamaño del archivo en bytes.
        f.write(dword(14 + 40 + anchoP * altoP * 3))
        f.write(dword(0)) #Cosa que no se utilizará en este caso.
        f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
        #Lo anterior suma 14 bytes.

        #Información del header.
        f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(anchoP)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(altoP)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
        f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
        f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(anchoP * altoP * 3)) #Tamaño de la imagen sin el header.
        #Pixels que no se usarán mucho.
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        #Lo anterior suma 40 bytes.

        #print("Framebuffer", framebuffer)

        #print(framebuffer[Posx][Posy])

        #Pintando el archivo de color negro.
        for x in range(altoP):
            for y in range(anchoP):
                f.write(framebuffer[y][x])



        f.close() #Cerrando el archivo que se escribió.
