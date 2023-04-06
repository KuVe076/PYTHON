print("*"*10)
print("Alimentación de Grogu")
print("*"*10)
galleta = float(input("Cantidad de Navarro Nummies consumidas (en unidades): "))
#cambio de unidad de [unidad] a [gramo]
uag = (galleta*11)
'''
Calculo grasas, carbohidratos y proteínas por galletas consumidas (por regla de 3)
    1 unidad equivale a 11 [g]
        1.90 [g] Grasas
        6.00 [g] Carbohidratos
        0.80 [g] Proteínas
'''
GrasaG = (uag*1.90)/11
CarbhG = (uag*6.00)/11
ProteG = (uag*0.80)/11
sopa = int(input("Space soup consumida (en [ml]): "))
'''
Calculo grasas, carbohidratos y proteínas por ml de sopa consumida (por regla de 3)
    1 porción equivale a 285 [ml]
        10.0 [g] Grasas
        12.0 [g] Carbohidratos
        11.0 [g] Proteínas
'''
GrasaS = (sopa*10)/285
CarbhS = (sopa*12)/285
ProteS = (sopa*11)/285
carne = int(input("Carne de rana consumida (en [g]): "))
'''
Calculo grasas, carbohidratos y proteínas por gramos de carne consumida (por regla de 3)
    1 porción equivale a 100 [g]
        0.30 [g] Grassa
        0.00 [g] Carbohidratos
        16.0 [g] Proteínas
'''
GrasaC = (carne*0.30)/100
CarbhC = (carne*0.00)/100
ProteC = (carne*16.0)/100
#Suma de Grasas totales redondeando a 2 decimales
GrasaT = round(float(GrasaC + GrasaG + GrasaS), 2)
#Suma de Carbohidratos totales redondeando a 2 decimales
CarbhT = round(float(CarbhC + CarbhG + CarbhS), 2)
#Suma de Proteínas totales redondeando a 2 decimales
ProteT = round(float(ProteC + ProteG + ProteS), 2)
'''
Calculo de calorias
    1 [g] Grasas = 9 [calorías]
    1 [g] Carbohidratos = 4 [calorías]
    1 [g] Proteínas = 4 [calorías]
'''
CalG = float((GrasaT*9))
Calch = float((CarbhT*4))
CalP = float((ProteT*4))

print("*"*10)
print("La cantidad de grasas que consumió Grogu fue:", GrasaT)
print("La cantidad de carbohidratos que consumió fue:", CarbhT)
print("La cantidad de proteínas que consumió fue:", ProteT)

CalT = round(float(CalG+Calch+CalP), 2)
print("Dando asi un total de:", CalT, "[calorias]")
print("*"*10)

'''
Caso 1:
**********
Alimentación de Grogu
**********
Cantidad de Navarro Nummies consumidas (en unidades): 4.3
Space soup consumida (en [ml]): 500
Carne de rana consumida (en [g]): 300
**********
La cantidad de grasas que consumió Grogu fue: 26.61
La cantidad de carbohidratos que consumió fue: 46.85
La cantidad de proteínas que consumió fue: 70.74
Dando asi un total de: 709.85 [calorias]

Caso 2:
**********
Alimentación de Grogu
**********
Cantidad de Navarro Nummies consumidas (en unidades): 7
Space soup consumida (en [ml]): 666
Carne de rana consumida (en [g]): 33
**********
La cantidad de grasas que consumió Grogu fue: 36.77
La cantidad de carbohidratos que consumió fue: 70.04
La cantidad de proteínas que consumió fue: 36.59
Dando asi un total de: 757.45 [calorias]
**********

Caso 3:
**********
Alimentación de Grogu
**********
Cantidad de Navarro Nummies consumidas (en unidades): 16
Space soup consumida (en [ml]): 519
Carne de rana consumida (en [g]): 163
**********
La cantidad de grasas que consumió Grogu fue: 49.1
La cantidad de carbohidratos que consumió fue: 117.85
La cantidad de proteínas que consumió fue: 58.91
Dando asi un total de: 1148.94 [calorias]
'''






