##Hacer un programa que determine si una persona es mayor de edad o no.

print("Bienvenido al taller nuemero 11:")

añ1=int(input("Ingresa el año actual: "))
añ2=int(input("Ingresa el año ene que naciste: "))

edad=añ1-añ2

print("Esta es tu edad:",edad)

if edad > 17:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")
