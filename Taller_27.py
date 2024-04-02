#27. Programa que muestre un menú que tenga las siguientes opciones: 
#1. Pasa o no la materia? 2. Es mayor o menor de edad? Caso 1: Solicitar 3 notas y determinar si el 
#promedio es mayor a 3.0, en ese caso el estudiante pasa. 
#Caso 2: Se debe solicitar el año de nacimiento y el año actual y determinar si es o no mayor de edad.

print('''
      ----------------------------------------
        menu
      1-Pasa o no la mataria.
      2-Es mayor o menor de edad.
      ----------------------------------------
      ''') 
num1=int(input("\nUsuario ingresa a una obcion: "))
if num1==1:
    num2=float(input("Ingresa nota 1: "))
    num5=float(input("Ingresa nota 2: "))
    num6=float(input("Ingresa nota 3: "))
    nota=(num2+num5+num6)/3
    if nota>=3.0:
        print("Este estudiante pasa.")
    else:
        print("Este estudiante pierde.")
elif num1==2:
    num3=int(input("Ingrese el año actual: "))
    num4=int(input("Ingrese  el año de nacimiento:  "))
    if num3-num4 <=18:
        print("Es mayor de edad.")
    else:
        print('Es menor de edad.')