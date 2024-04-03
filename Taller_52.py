#52. Programa que permita solicitar 15 nombres, almacenarlos en un vector y luego los muestre en 
#el orden ingresado. 

nombres = [0] * 15

for i in range(15):
    persona = (input("Digite el nombre de las personas " + str(i + 1) + ": "))
    nombres[i] = persona

print("\nNombres ingresados: ")
for i in range(15):
    print("Nombre de las personas" + str(i + 1) + ": " + str(nombres[i]),".")
