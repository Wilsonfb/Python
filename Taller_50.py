#50. Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción Salir. Las opciones del menú deben permitir:    
#1. Números pares hasta 100 (usando for) 2. Múltiplos de 4 (usando while) 3. Tabla de Multiplicar de un número hasta 10  

seguir = True
            
while seguir:
    print('''
      ----------------------------------------
        menu
      1-Números pares hasta 100.
      2-Múltiplos de 4.
      3-Tabla de Multiplicar de un número hasta 10.
      4-Salir.
      ----------------------------------------
      ''') 
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        for i in range(1, 101):
            if i%2 == 0:
                print (i)
    elif opcion == 2:
        i = 0
        while i < 100:
            i+=1
            if i%4 == 0:
                print(i)
    elif opcion == 3: 
        num1 = float (input("Digite un numero: "))
        for i in range(1, 11):
            tabla = num1 * i
            print(f"{num1} * {i} : {tabla}.")
    elif opcion == 4:
        print("Saliste.")
        seguir = False
    else:
        print("Error.")
