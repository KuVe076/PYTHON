def obtener_valor_característica(características, buscada):
   valor = 0
   for x, y in características:
      if x == buscada:
         valor = y
   return valor

def puntaje_amigo(amigo, caracteristica):
   valor = 0
   _,caracteristicas_amigo = amigo
   for i in range(len(caracteristicas_amigo)):
      carac = caracteristicas_amigo[i]
      k = obtener_valor_característica(características, carac)
      valor += k 
   return valor

características = [('kawaii',10),('leal',20),('acusete',-10),
('avaro',-15),('respetuoso',20),('otaku',25),
('lolero',25),('furro',-50),('vtuver',25),
('mechero',-30)]

amigos = [('Mojojojo',('mechero','kawaii','furro','lolero')),
 ('Otaku-taku',('otaku','avaro','lolero','leal')),
 ('Maiga',('paciente','otaku','leal')),
 ('Seiya',('leal','acusete')),
 ('Vegeta',('otaku','avaro')),
 ('Sneki',('leal','kawaii','vtuver')),
 ('Kalila',('lolero','kawaii')),
 ('Grogu',('avaro','kawaii','lolero','otaku')),
 ('Freezer',('acusete','furro','otaku','lolero'))]


loleros = []

for x in amigos:
   nombre_amigo = x[0]
   caracteristica_amigo = x[1]
   if "lolero" in caracteristica_amigo:
      pje = puntaje_amigo(x,características)
      loleros.append((pje, nombre_amigo))
loleros.sort()
loleros.reverse()
   

print(obtener_valor_característica(características, "vtuver"))
print(obtener_valor_característica(características, "puntual"))
print(puntaje_amigo(('Vegeta',('otaku','avaro')),características))
print("Equipo seleccionado:")
print(loleros[0][1]+ ",", loleros[0][0],"puntos")
print(loleros[1][1]+ ",",loleros[1][0],"puntos")