#48. Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción salir. Las opciones del menú deben permitir:       
#1. Ingresar 2 números 2. Realizar la suma 3. Realizar la resta 4. Realizar la multiplicación 5. Realizar la división 6. Salir del programa 

continuar = True

while continuar:
    print('''
      ----------------------------------------
        menu
      1-Ingresar 2 números.
      2-Realizar la suma.
      3-Realizar la resta.
      4-Realizar la multiplicacion.
      5-Realizar la division.
      6-Salir del programa.
      ----------------------------------------
      ''') 
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        num1 = int(input("Digite un numero: "))
        num2 = int(input("Digite un numero: "))
    elif opcion == 2:
        suma = num1+num2
        print(f"El resultado de la suma es {suma}.")
    elif opcion == 3:
        resta = num1-num2
        print(f"El resultado de la resta es {resta}.")
    elif opcion == 4:
        multiplicacion = num1*num2
        print(f"El resultado de la multiplicacion es {multiplicacion}.")
    elif opcion == 5:
        divicion = num1/num2
        print(f"El resultado de la divicion es {divicion}.")
    elif opcion == 6:
        continuar = False
        print("Saliste del programa")
    else: 
        print("Error")