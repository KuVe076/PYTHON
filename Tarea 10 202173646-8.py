def avistamientos_por_región(nombre_archivo):
    archivo_principal = open(nombre_archivo,"r",encoding='utf-8')
    diccionario_regiones = {}
    saltar_linea = True

    for i in archivo_principal:
        if not saltar_linea:
            linea = i.strip().split(";")
            fecha_mes = linea[0][5:]
            fecha_año = linea[0][0:4]
            nombre_region = linea[1]
            casos_totales = int(linea[2])
            casos_ovnis = int(linea[3])
            
            porcentaje_ovnis = round(((casos_ovnis/casos_totales)*100),2)
            
            datos = porcentaje_ovnis,fecha_mes,fecha_año,casos_totales,casos_ovnis
            
            if nombre_region not in diccionario_regiones:
                diccionario_regiones[nombre_region] = []
            diccionario_regiones[nombre_region].append(datos)
        saltar_linea = False
    
    for region in diccionario_regiones:
        diccionario_regiones[region].sort(reverse=True)
        
        archivo_escrito = open(region+".txt","w")
        
        contador = 0
        for porcentaje,mes,año,totales,ovnis in diccionario_regiones[region]:
            if contador <= 2:
                archivo_escrito.write(f"En el mes {mes} de {año} hubo {porcentaje}% de avistamientos confirmados de un total de {totales}\n")
                contador += 1
        archivo_escrito.close()
    archivo_principal.close()
    return len(diccionario_regiones)

print(avistamientos_por_región('ovnis_grande.csv'))
