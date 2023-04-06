def nf_aritmet(c1,c2,c3):
    prom = round(float((c1+c2+c3)/3))
    return prom

def nf_geo(c1,c2,c3):
    geometrica = round(float(((c1*c2*c3)**(1/3))))
    return geometrica

def nf_vuelt(c1,c2,c3):
    valor = (nf_aritmet(c1,c2,c3))
    vuelta = round(float(((valor)**2)*n3)**(1/3))
    return vuelta

def nf_aprob(f1,f2,f3):
    if f1 >= 55:
        return 1
    elif f2 >= 55:
        return 2
    elif f3 >= 55:
        return 3
    else:
        return 0
    
    
pedir_notas = True
while pedir_notas:
    ramo = input("Ingrese el nombre del ramo: ")

    if ramo == "salir":
        pedir_notas = False
        print("Fin del programa - Desarrollado por Kiwi :D!")
    else:
        n1 = int(input("Ingrese la 1era nota: "))
        n2 = int(input("Ingrese la 2era nota: "))
        n3 = int(input("Ingrese la 3era nota: "))

        nf_aritmetica = nf_aritmet(n1,n2,n3)
        nf_geometrica = nf_geo(n1,n2,n3)
        nf_vuelta = nf_vuelt(n1,n2,n3)

        print("Su nota final según la Media Aritmética es:", nf_aritmetica)
        print("Su nota final según la Media Geométrica es:", nf_geometrica)
        print("Su nota final según la Media Vuelta es:", nf_vuelta)

        nf_aprobacion = nf_aprob(nf_aritmetica,nf_geometrica,nf_vuelta)

        if nf_aprobacion == 0:
            print("Lamentablemente no puedes aprobar con ninguna de las fórmulas :'c")
        elif nf_aprobacion == 1:
            print("Si la NF del ramo se calcula usando la Media Aritmética, entonces apruebas", ramo, ":D")
        elif nf_aprobacion == 2:
            print("Si la NF del ramo se calcula usando la Media Geométrica, entonces apruebas", ramo, ":D")
        elif nf_aprobacion == 3:
            print("Si la NF del ramo se calcula usando la Media Vuelta, entonces apruebas", ramo, ":D")
