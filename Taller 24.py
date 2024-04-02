#Hacer un codigo que permita determinar si una letra es o no vocal.

print("Bienvenido al taller numero 24.")

#Hacer un codigo para saber que son vocales.

def son_vocales(letra):
    switch = {"a":True,"e":True,"i":True,"o":True,"u":True} 
    return switch.get(letra.lower(), False)

#Preguntar la letra.

letra=input("Digite la letra en minuscula si que quiere saber si es vocal o no: ")

#Saber si es vocal o no.
if son_vocales(letra):
    print("La letra",letra,"es una vocal.")
else:
    print("La letra",letra,"no es vocal.")
