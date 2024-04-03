#61. Programa que permita solicitar 25 nombres y 25 apellidos y los muestre en forma de un único 
#listado 

nom = []
apell = []

for i in range(25):
    nombre = input(f"Digite el nombre {i+1}: ")
    nom.append(nombre)

for i in range(25):
    apellido = input(f"Digite el apellido {i+1}: ")
    apell.append(apellido)

for nombre, apellido in zip(nom, apell):
    print(f"{nombre} {apellido}")
    
