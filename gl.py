"""
#Nombre: Javier Valle
#Carnet: 20159

Referencias: 

1. Instanciar un archivo de Python: https://www.youtube.com/watch?v=rYcluou5gEo&ab_channel=LuisCabreraBenito
2. Saber si un número es múltiplo de otro: https://www.youtube.com/watch?v=jOCh6ZpkE1k&ab_channel=JohnOrtizOrdoñez
3. Hacer un return de múltiples variables: https://www.youtube.com/watch?v=QOQTYuynU3w&ab_channel=ProgramaResuelto
4. Formato de archivo BMP: https://en.wikipedia.org/wiki/BMP_file_format#:~:text=The%20BMP%20file%20format%2C%20also,and%20OS%2F2%20operating%20systems. 
5. Acceder a una variable de otra clase: https://programmerclick.com/article/14131486210/
"""

import Render as Rend #Importando la clase Render.
from utilidades import *

#Variables globales.
anchoV = 0 #Ancho de la ventana.
altoV = 0 #Alto de la ventana.


#Color de la pantalla.
rP = 0
gP = 0
bP = 0
fondo = 0

#Variable global para la función glColor.
Color = 0

#Render = None #Instanciando la clase de Render.

#Pregunar si está bien implementada esta función.
def glInit(): #Se usará para poder inicializar cualquier objeto interno que requiera el software de render.

    #Importar la clase de Render.
    #r = Render.Render(ancho, alto, glClear(), glColor(0.003, 1, 0.019)) #Creando el color de la línea.) #Creando el framebuffer con el color que se le pasa.
    pass

def glCreateWindow(width, height): #Preguntar de esta función.
    #Se usará para inicializar el framebuffer con un tamaño (la imagen resultante va a ser de este tamaño)
    global anchoV, altoV #Variables globales, que servirán para definir el tamaño de la imagen resultante.

    try: #Verificar que el tamaño sea un número.
        #Saber si las dimensiones son múltiplos de 4.
        if width % 4 == 0 and height % 4 == 0:
            
            #Llenando variables globales. Estas son para el ancho de la ventana y el alto de la ventana.
            anchoV = width 
            altoV = height

            Rend.DimensionesPantalla(anchoV, altoV) #Creando la ventana.

        elif width < 0 or height < 0: #Si las dimensiones son negativas, entonces se imprime un error.
            print("Error")
        else: 
            print("Error")
    
    except (TypeError, ZeroDivisionError): #Si en caso es NoneType, entonces se imprime esta excepción.
        print("Ocurrió un problema con el tamaño de la imagen.")
    #except: #Si en caso se escribió una letra en vez de número, entonces se imprime esta excepción.
     #   print("Se ingresó una letra en vez de número.")


#Preguntar si esta función lo que hace es llenar por primera vez el color de la pantalla.
def glClear(): #Se usará para que llene el mapa de bits con un solo color.   
    global fondo #Variable global para el color del fondo de pantalla.
    
    fondo = color(rP, gP, bP) #Creando el color de la línea.

    Rend.recibirColorFondo(fondo) #Recibiendo el color del fondo.
    Rend.Framebuffer() #Llenando el framebuffer de la pantalla.

def glClearColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
    
    global rP, gP, bP #Se usa para poder acceder a las variables globales.

    #global Render #Se usa para poder acceder a la variable global render.
    
    #Llenando variables globales.
    rP = r
    gP = g
    bP = b


def glVertex(x, y): #Función que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort. glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina superior derecha. glVertex(-1, -1) la esquina inferior izquierda
    #Ubicar un punto en el viewport.

    #Bucket fill.

    Rend.Vertex(x, y) #Creando el punto.

def line(x0,y0,x1, y1): #Función que pueda dibujar una línea.
    
    #Calculando cambios.
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    #print("Cambio en x y cambio en y: ", dx, dy)

    steep = dy > dx #Variable que mide si dy es más grande que dx.

    if steep: #Si dy es mayor que dx, entonces se cambia el valor de x y y.
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    
    if x0 > x1: #Si x0 es mayor que x1, entonces se cambian los valores de x0 y x1.
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #Calculando los nuevos cambios.
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    #print("Cambio en x y cambio en y: ", dx, dy)
    offset = 0 #Offset de la línea.
    threshold = dx #Variable que mide el cambio en x.
    y = y0 #Variable que mide la coordenada y.

    #Dibujando la línea.
    for x in range(x0, x1): #Recorriendo el rango de x0 a x1.
        offset += dy * 2 #Incrementando el offset.
        if offset >= threshold:
            y += 1 if y0 < y1 else -1
            threshold += 2 * dx #Incrementando el threshold.
        
        #print("Punto inicual: ", x0, y0)
        #print("Punto final: ", x1, y1)
        
        if steep: #Si la línea es vertical, entonces se cambia el valor de x y y.
            Rend.Vertex(y, x) #Creando la línea.
        else: #Si la línea es horizontal, entonces se cambia el valor de x y y.
            Rend.Vertex(x, y) #Creando la línea.

def glColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.
    
    global Color #Se usa para poder acceder a las variables globales.
    
    Color = color(r, g, b) #Se manda a hacer el color con las utilidades y se setea el color.
    print(Color)
    Rend.colorPunto(Color)
    #print("El color del punto es: ", Color)

def glFinish(): #Función que escribe el archivo de imagen resultante.

   #Rend.punto(25, 25) #Probando el método punto.
   Rend.write() #Escribiendo el archivo.
