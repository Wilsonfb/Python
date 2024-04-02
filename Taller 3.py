##Hacer un programa para calcular la distancia recorrida en un movimiento rectilíneo.

print("Bienvenido al taller 3.")
def disre(vel, tie):
    dis= vel * tie
    return dis
vel= float(input("Ingresa la velocidad:"))
tie = float(input("Ingresa el tiempo:"))
dis = disre(vel, tie)
print("La distancia recorrida es:", dis)
