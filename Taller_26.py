#26. Programa que permita ingresar un número cualquiera y luego mostrar el siguiente menú: 
#1. Determinar si es positivo o negativo 2. Determinar si es par o impar 
#El programa debe realizar las operaciones que el usuario seleccione del menú

print('''
      ----------------------------------------
        menu
      1-Determinar si es positivo o negativo.
      2-Determinar si es par o impar.
      ----------------------------------------
      ''')
num1=int(input("\nUsuario ingresa a una obcion"))
if num1==1:
    num2=int(input("Ingresa un numero para validar: "))
    if num2 <= 0:
        print("Este", num2, " es negativo.")
    else:
        print("Este ",num2," es positivo.")
elif num1==2:
    num3=int(input("Ingresa un numero: "))
    if not(num3 / 2) == True:
        print("El ",num3, " es par.")
    else:
        print('es impar')


    