'''
def emoji(text):
    i = 0
    while i < len(text) and text[i] != "*":
        i += 1
    return text[:i]

def emodefinicion(sign):
    i = 0
    j = 0
    while i < len(sign) and sign[i] != "$":
        if sign[i] == "*":
            j = i
        i += 1
    return sign[j+1:i]

def clear(text):
    i = 0
    while i < len(text) and text[i] != "$":
        i += 1
    return text[i+1:]

def reemplazo(text,emoji,definicion):
    largo_emoji = len(emoji)
    i = 0
    texto_final = text * 1
    while i < len(texto_final) - largo_emoji + 1:
        if emoji == texto_final[i:i+largo_emoji]:
            texto_final = texto_final[:i] + definicion + texto_final[i+largo_emoji:]
        i += 1
    return texto_final

texto = input("Ingrese texto: ")
Significado = input("Ingrese el significado de sus emoticones: ")

while Significado != "":
    Emoji= emoji(Significado)
    Significado_Emoji = emodefinicion(Significado)
    Significado_Emoji = Significado_Emoji.upper()
    Significado = clear(Significado)
    Frase_Cambiada = reemplazo(texto, Emoji, Significado_Emoji)
    texto = Frase_Cambiada

print(Frase_Cambiada)

'''

certamen_1 = int(input("certamen 1"))
certamen_2 = int(input("certamen 2"))
certamen_3 = int(input("certamen 3"))

control_1 = int(input("control 1"))
control_2 = int(input("control 2"))
control_3 = int(input("control 3"))

promedio_certamenes = 0.8*((certamen_1+certamen_2+certamen_3)/3)
promedio_controles = 0.2*((control_1+control_2+control_3)/3)

final = promedio_certamenes+promedio_controles
print(final)


    

    

