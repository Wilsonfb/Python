#Hacer un programa para determinar si un número cualquiera ingresado por el usuario es o no positivo.

print("Bienvenido al taller numero 12.")

num=int(input("Digite el numero que quieres saber si es positivo o negativo: "))

if num>0:
    print("El numero que ingresaste es positivo:")
elif num==0:
    print("El numero que ingresaste es cero:")
else:
    print("El nuemro que ingresaste es negativo:")
