import re
import numpy as np
from PIL import Image


instruction = "Izquierda|Derecha|(Avanzar)( (\d+))?|(Pintar\s)(Rojo|Verde|Azul|Negro|Blanco|RGB\((([0-9]{1,3}),([0-9]{1,3}),([0-9]{1,3}))\))|(Repetir) (\d+)+ veces {\s(.*)\s}| "

finder = re.compile(instruction)

class flag:
    def __init__(self,value):
        self.value = value

    def change_flag(self,new):
        '''
        Modifica el valor de self.value con True o False 

            Parametros:
                    new (bool): True o False
        '''
        self.value = new
    
    def get_value(self):

        '''
        Obtiene el valor de flag
        '''    

        return self.value

boolean_flag = flag(True) 

class paper:
    def __init__(self, dim, background):
        self.dim = dim
        fila = []
        for x in range(dim):
            fila.append(background)
        self.matriz = []
        for x in range(dim):
            self.matriz.append(fila.copy())
        self.position = [0,0]
        self.direction = [1,0]
    
    def move_pixel(self , n):

        '''
        Modifica el valor de self.position para que asi el cursor se desplace por la matriz

            Parametros:
                    n (int): numero de veces que debera avanzar
        '''
        i = 0
        while i < n:
            self.position[0] += self.direction[0] 
            self.position[1] += self.direction[1]
            i += 1 

        if self.position[0] >= self.dim or self.position[0] < 0 or self.position[1] >= self.dim or self.position[1] < 0:
            raise Exception


    def tright(self):
        
        '''
        Modifica el valor de self.direction para que asi el cursor gire a la derecha

        '''
        self.direction = [-1*(self.direction[1]),self.direction[0]]

    def tleft(self):

        '''
        Modifica el valor de self.direction para que asi el cursor gire a la izquierda

        '''
        self.direction = [(self.direction[1]),-1*(self.direction[0])]
         
    def paint_pixel(self ,color):

        '''
        Pinta un pixel del lienzo

            Parametros:
                    color (tuple): 3-tupla la cual contiene el (R,G,B) con el que se pintara el pixel 
        '''

        x = self.position[0]
        y = self.position[1]
        self.matriz[y][x] = color

def Color(color):
    '''
    Obtiene un string el cual es es usado como llave para acceder a un valor de 3-tuplas

        Parametros:

            color(str): Color el cual sera usado para obtener la 3-tupla
        
        Retorno:

            colors(int): 3-tupla con los valores utilizados para el RGB
    '''
    colors ={"Rojo":(255,0,0), "Verde":(0,255,0), "Azul":(0,0,255), "Negro":(0,0,0), "Blanco":(255,255,255)}
    return colors[color]
  
def MatrizAImagen(matriz, filename='pixelart.png', factor=10):

    '''
    Convierte una matriz de valores RGB en una imagen y la guarda como un archivo png.
    Las imagenes son escaladas por un factor ya que con los ejemplos se producirian imagenes muy pequeñas.
        
        Parametros:
                
                matriz (lista de lista de tuplas de enteros): Matriz que representa la imagen en rgb.
                filename (str): Nombre del archivo en que se guardara la imagen.
                factor (int): Factor por el cual se escala el tamaño de las imagenes.
    '''

    matriz = np.array(matriz, dtype=np.uint8)
    np.swapaxes(matriz, 0, -1)

    N = np.shape(matriz)[0]

    img = Image.fromarray(matriz, 'RGB')
    img = img.resize((N*10, N*10), Image.Resampling.BOX)
    img.save(filename)

def Repeat(actions, times):

    '''
    Agrega a una lista n veces las acciones que se encuentran dentro de los {} 

        Parametros:

                actions(str): acciones que se encuentran dentro de los {}
                times(str): numero de veces las cuales se repite una opción

        Retorno:

            Retorna una lista con las acciones que se deberan realizar
    '''
    
    i = 0
    r_actions = []
    while i < int(times):
        r_actions.append(actions)
        i += 1
    return r_actions

def actions(line, num_line):

    '''
    Lee una linea la cual es entregada y obtiene un string, con el cual se compara con los siguientes str (Avanzar, Derecha, Izquierda, Pintar ,
    Repetir), en caso de que la comparación sea valida se realizara una de las funciones designadas en la clase paper(move_pixel, tright, tleft, paint_pixel)
        
        Parametros:
                
                line (str): lineas que contiene el archivo codigo.txt
                num_line (int): Numero de cada linea correspondiente al archivo
    '''

    pos = 0

    while pos < len(line):

        action = finder.match(line,pos)

        if action == None:
            
            error_file.write(str(num_line)+" "+line+"\n")
            boolean_flag.change_flag(False)
            break

        else:

            pos += len(action.group(0))

            if action.group(1) == 'Avanzar':
            
                if action.group(3) == None:
                    
                    try:
                        pixelart.move_pixel(1)

                    except Exception: 
                        print(str(num_line)+' Fuera de los limites')
                        exit()
                    
                else:
                    try:
                        pixelart.move_pixel(int((action.group(3))))
                    
                    except Exception:
                        print(str(num_line)+' Fuera de los limites')
                        exit()
                
                    
            elif action.group(0) == 'Derecha':
            
                pixelart.tright()
                
            elif action.group(0) == 'Izquierda':
                
                pixelart.tleft()

            elif action.group(4) == 'Pintar ':

                if 'RGB' in action.group(5):
                    pixelart.paint_pixel((int(action.group(7)), int(action.group(8)), int(action.group(9))))
                
                else:
                    pixelart.paint_pixel(Color(action.group(5)))

            elif action.group(10) == 'Repetir':

                multi_task = Repeat(action.group(12),action.group(11))
                
                for x in range(int(action.group(11))):
                    actions(multi_task[0], wrong_line)

file = open("codigo.txt","r",encoding='utf-8')

wrong_line = 0

error_file = open("errores.txt","w",encoding='utf-8')

first_line = file.readline()

width_match = re.match("Ancho\s(\d+)",first_line)

width = 2

if width_match != None:

    width = width_match.group(1)

else:
    error_file.write("1 "+first_line)
    boolean_flag.change_flag(False)

wrong_line +=1


second_line = file.readline()

color = re.match("Color de fondo (Rojo|Verde|Azul|Negro|Blanco|RGB\((([0-9]{1,3}),([0-9]{1,3}),([0-9]{1,3}))\))",second_line)

background = (0,0,0)

if color != None:

    if color.group(1) in ["Rojo", "Verde", "Azul", "Negro", "Blanco"]:
        
        background = Color(color.group(1))

    else:
    
        background = (int(color.group(3)), int(color.group(4)), int(color.group(5)))

else:
    error_file.write("2 "+second_line)
    boolean_flag.change_flag(False)

wrong_line += 1

blank_space = file.readline()

if blank_space != '\n':
    error_file.write("3 "+blank_space)
    boolean_flag.change_flag(False)

wrong_line += 1

pixelart = paper(int(width), background)

for lines in file:
   
    lines = lines.strip()
    wrong_line += 1
    actions(lines, wrong_line)
   
if boolean_flag.get_value():
    error_file.write("No hay errores!")
    MatrizAImagen(pixelart.matriz)

print(pixelart.matriz)

error_file.close()
file.close()


'''
Nombre: Gonzalo Andres Alarcón Carrasco
ROL: 202173646-8
'''