##########################################
#                                        #
#  Programe sus funciones aquí           #
#                                        #
##########################################

def disparo(tablero, barcos, fila, columna):
    for j in barcos:
        i = 0
        largo_barco = int(j[0])
        orientacion = int(j[1])
        fila_barco = int(j[2])
        columna_barco = int(j[3])
        while i < largo_barco and fila_barco < 9 and columna_barco < 9:
            if fila_barco == fila and columna_barco == columna:
                tablero[fila][columna] = "O"
                return 0
            if orientacion == 1:
                (fila_barco) += 1
            elif orientacion == 2:
                (columna_barco) += 1
            i +=1
        tablero[fila][columna] = " "
    return 0 
    
def destruidos(tablero, barcos):
    barcos_explotados = 0
    for j in barcos:
        i = 0
        count = 0
        barco_destruido = []
        largo_barco = int(j[0])
        orientacion = int(j[1])
        fila_barco = int(j[2])
        columna_barco = int(j[3])
        while i < largo_barco and fila_barco < 9 and columna_barco < 9:
            if tablero[fila_barco][columna_barco] == "O":
                count += 1
                l1 = [fila_barco,columna_barco]
                barco_destruido.append(l1)
                if count == largo_barco:
                    for x in barco_destruido:
                        tablero[x[0]][x[1]] = "X"
            if tablero[fila_barco][columna_barco] == "X":
                barcos_explotados += 1
                break 
            if orientacion == 1:
                (fila_barco) += 1
            elif orientacion == 2:
                (columna_barco) += 1
            i +=1
    return barcos_explotados


# OPCIONAL:
# Cambie el valor de esta variable a 1 si desea ver
# la ubicación de los barcos antes de comenzar.
# Esto puede ser útil para probar sus funciones.
mostrar_solucion = 0



##################################################
#                                                #
#  NO MODIFIQUE EL CÓDIGO A PARTIR DE ESTE PUNTO #
#                                                #
##################################################

import random as rd

# Función que muestra el tablero con el formato deseado para la pantalla
def show(tablero):
    print("\n  123456789")
    for i in range(9):
        fila_texto = " "
        for j in tablero[i]:
            fila_texto += str(j)
        print(chr(65+i)+fila_texto)

# Creación del tablero (inicialmente únicamente con "-" en todas las posiciones)
tablero = []
board = []
for i in range(9):
    fila = []
    for j in range(9):
        fila.append("-")
    tablero.append(fila)
    board.append(list(fila))

# Creación de los barcos con orientación y posición aleatorias
barcos = []
length = [2,3,3,4,5]
for i in range(5):
    l = length[i]
    orientation = rd.randint(1,2)
    if orientation == 1:
        flag = True
        while flag:
            row = rd.randint(0,9-l)
            column = rd.randint(0,8)
            empty = True
            for j in range(l):
                empty = empty and board[row+j][column] != "X"
            if empty:
                flag = False
        for j in range(l): board[row+j][column] = "X"
    else:
        flag = True
        while flag:
            row = rd.randint(0,8)
            column = rd.randint(0,9-l)
            if "X" not in board[row][column:column+l]:
                flag = False
        for j in range(l): board[row][column+j] = "X"
    barcos.append([l,orientation,row,column])
#print(barcos)
# Se muestra la solución al inicio en caso de que se haya seleccionado esta opción
if mostrar_solucion == 1:
    print("Solución:")
    show(board)
    print("\n\n")

# Ciclo principal del programa donde se reciben los disparos, se validan y se llama a la función disparo()
print("¡Bienvenido a Solitary Battleship!")
destroyed = 0
while destroyed < 5:
    not_valid = True
    while not_valid:
        turn = input("\n¿Que casilla desea disparar? (Ejemplo: A1): ")
        not_valid = False
        if len(turn) != 2:
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("A" <= turn[0] and turn[0] <= "I"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("1" <= turn[1] and turn[1] <= "9"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        else:
            fila = "ABCDEFGHI".index(turn[0])
            columna = int(turn[1])-1
            if tablero[fila][columna] != "-":
                not_valid = True
                print("Ya ha disparado a esta casilla.")
    disparo(tablero, barcos, fila, columna)
    destroyed = destruidos(tablero, barcos)
    show(tablero)
    print("\n"+str(destroyed)+" barcos destruidos.")
    # Fin del juego
    if destroyed == 5:
        print("Felicidades, juego terminado.")

