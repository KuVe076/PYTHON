from math import sqrt
flag = False
carne = int(4000)
vege = int(3000)
vega = int(3500)
seguir = True
plato = 1
pedido = 0
precio_final = 0

Sucursal1 = input("Ingrese nombre de la sucursal 1: ")
Cx1 = int(input("Coordenada X: "))
Cy1 = int(input("Coordenada Y: "))

Sucursal2 = input("Ingrese nombre de la sucursal 2: ")
Cx2 = int(input("Coordenada X: "))
Cy2 = int(input("Coordenada Y: "))

Sucursal3 = input("Ingrese nombre de la sucursal 3: ")
Cx3 = int(input("Coordenada X: "))
Cy3 = int(input("Coordenada Y: ")) 

Sucursal1_pedido = 0
Sucursal2_pedido = 0
Sucursal3_pedido = 0

while not flag:
    while seguir:
        plato_deseado = int(input("Ingrese número del plato: "))
        if plato_deseado == 1:
            pedido += carne
        elif plato_deseado == 2:
            pedido += vege
        elif plato_deseado == 3:
            pedido += vega
        elif plato_deseado == -1:
            seguir = False
    precio_final += pedido
    print("Total del pedido $", pedido)

    Coordenada_clientex = int(input("Ingrese coordenada x cliente: "))
    Coordenada_clientey = int(input("Ingrese coordenada y cliente: "))
    
    suma_distancia1 = int(((Coordenada_clientex-Cx1)**2)+((Coordenada_clientey-Cy1)**2))
    distancia1 = int(sqrt(suma_distancia1))
    
    suma_distancia2 = int(((Coordenada_clientex-Cx2)**2)+((Coordenada_clientey-Cy2)**2))
    distancia2 = int(sqrt(suma_distancia2))
    
    suma_distancia3 = int(((Coordenada_clientex-Cx3)**2)+((Coordenada_clientey-Cy3)**2))
    distancia3 = int(sqrt(suma_distancia3))
    
    if distancia1 < distancia2 and distancia1 < distancia3:
        print("Pedido será entregado por: ", Sucursal1)
        Sucursal1_pedido +=1
    
    elif distancia2 < distancia1 and distancia2 < distancia3:
        print("Pedido será entregado por: ", Sucursal2)
        Sucursal2_pedido +=1
    
    elif distancia3 < distancia2 and distancia3 < distancia1:
        print("Pedido será entregado por: ", Sucursal3)
        Sucursal3_pedido +=1 
    
    continuar = input("¿Desea registrar otro pedido?: ")
    
    if continuar == "Si":
        flag = False
    
    else:
        flag = True
    seguir = True
    
    pedido = 0

print("#"*5, "Estadisticas Finales", "#"*5)
print("Monto total recaudado $", precio_final)
print(Sucursal1, "entregó", Sucursal1_pedido, "pedidos")
print(Sucursal2, "entregó", Sucursal2_pedido, "pedidos")
print(Sucursal3, "entregó", Sucursal3_pedido, "pedidos")




