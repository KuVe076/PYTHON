vacunas = {
 "Sinovac":["11.111.111-1", "12.345.678-9"],
 "Pfizer": ["8.978.657-3"],
 "CanSino": ["13.789.456-k"]
}
#{}

dosis = {
 "11.111.111-1":[55,(2021,4,11),(2021,5,10)],
 "12.345.678-9":[47,(2021,6,3)],
 "8.978.657-3":[79,(2021,3,23)],
 "13.789.456-k":[40,(2021,5,18),(2021,6,10)]
}
#{}
dia = input("Ingrese día: ")
mes = input("Ingrese mes: ")
año = input("Ingrese año: ")
fecha_vacunacion = año,mes,dia
flag = True
cuenta = {}
l1 = []

while flag:
    rut = input("Ingrese Rut: ")
    if rut not in dosis:
        edad = int(input("Ingrese edad: "))
        vacuna = input("Ingrese nombre vacuna: ")
        if vacuna not in vacunas:
            vacunas[vacuna] = []
        vacunas[vacuna].append(rut)
        dosis[rut] = [edad,fecha_vacunacion]
    else:
        for k in vacunas:
            if rut in vacunas[k]:
                print("Segunda dosis. Paciente debe ser inoculado con:",k)
        dosis[rut].append(fecha_vacunacion)
        
    seguir = input("¿Desea continuar? (s/n): ")
    if seguir == "n":
        flag = False

for x in dosis:
    if len(dosis[x]) == 3:
        edad_fecha = dosis[x]
        if edad_fecha[0] not in cuenta:
            cuenta[edad_fecha[0]] = 0
            cuenta[edad_fecha[0]] += 1
        else:
            cuenta[edad_fecha[0]] += 1
for i in cuenta:
    lista_conteo = (cuenta[i], i)
    l1.append(lista_conteo)
l1.sort()
l1.reverse()

print("Edades con más personas con esquema de inoculación completo:")
print(l1[0][1],"años:", l1[0][0],"persona")
print(l1[1][1],"años:",l1[1][0],"persona")
print(l1[2][1],"años:",l1[2][0],"personas")
