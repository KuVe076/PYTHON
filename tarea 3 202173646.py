print("*"*10)
print("Simulador de créditos hipotecarios del Banco de Pythonia")
print("*"*10)

valorp = int(input("Ingrese valor de la propiedad en UF (1500-13000):"))
if 1500<=valorp<=13000:
    pie = int(input("Ingrese % del pie (20%-45%):"))
    if 20<=pie and pie<=45:
        plazo = int(input("Ingrese plazo (20, 25, 30):"))
        if plazo == 20 or plazo == 25 or plazo == 30:
            tipo = int(input("Tipo de vivienda Casa (1) o Departamento (2):"))
            if tipo == 1 or tipo == 2:
                estado = int(input("Estado vivienda Nueva (1) o Usada (2):"))
                if estado == 1 or estado == 2:
                    vmp = int(valorp-(valorp*(pie/100)))
                    if plazo == 20:
                        if tipo == 1:
                            if estado == 1:
                                valor_mas_interes = float(vmp+(vmp*25/100))
                            elif estado == 2:
                                valor_mas_interes = float(vmp+(vmp*22/100))
                        elif tipo == 2:
                            if estado == 1:
                                valor_mas_interes = float(vmp+(vmp*28/100))
                            elif estado == 2:
                                valor_mas_interes = float(vmp+(vmp*26/100))
                    elif plazo == 25:
                        if tipo == 1:
                            if estado == 1:
                                valor_mas_interes = float(vmp+(vmp*30/100))
                            elif estado == 2:
                                valor_mas_interes = float(vmp+(vmp*27/100))
                        elif tipo == 2:
                            if estado == 1:
                                valor_mas_interes = float(vmp+(vmp*33/100))
                            elif estado == 2:
                                valor_mas_interes = float(vmp+(vmp*32/100))
                    elif plazo == 30:
                        if tipo == 1:
                            if estado == 1:
                                valor_mas_interes = float(vmp+(vmp*35/100))
                            elif estado == 2:
                                valor_mas_interes = float(vmp+(vmp*31/100))
                        elif tipo == 2:
                            if estado == 1:
                                valor_mas_interes = float(vmp+(vmp*41/100))
                            elif estado == 2:
                                valor_mas_interes = float(vmp+(vmp*37/100))
                    #Calculo seguros
                    insis = float(0)
                    bank = float(0)
                    if (tipo == 1 or tipo == 2) and estado == 1:
                        insis = float(0.8)
                    if tipo == 2:
                        bank = float(0.3)
                    sumcred = float(insis+bank+0.5)
                    
                    seg = int(sumcred*12*plazo)

                    Monto = round(float(valor_mas_interes+seg),2)
                    dividendo = round(float(Monto/(12*plazo)),2)

                    print("*"*10)
                    print("Total del credito a pagar:", Monto, "UF")
                    print("Dividendo mensual de", dividendo, "UF")
                    print("*"*10)
                else:
                    print("Error: Estado invalido")
            else:
                print("Error: Tipo invalido")
        else:
            print("Error: Plazo invalido")
    else:
        print("Error: Pie invalido")
else:   
    print("Error: Valor invalido")
