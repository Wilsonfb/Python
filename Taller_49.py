#49. Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción Salir. Las opciones del menú deben permitir:    
#1. Calcular el factorial de un número (usando un ciclo repetitivo for) 2. Calcular la potencia (usando un ciclo repetitivo while) 3. Salir 

continuar = True

while continuar:
    print('''
      ----------------------------------------
        menu
      1-Calcular el factorial de un número.
      2-Calcular la potencia.
      3-Salir.
      ----------------------------------------
      ''') 

    opcion = int(input("Elige alguna opción del menu: "))
    if opcion == 1:
        n = int(input("Digita un numero positivo: "))
        if n < 0:
            print("Error")
            n = int(input("Digita un numero positivo: "))
        else:
            resultado = 1
            for i in range(n):
                resultado *= n
                n -= 1
        print(f"El factorial es {resultado}.")
    elif opcion == 2:

        resultado = 1
        contador = 0

        base = float(input("Ingresa la base: "))
        exponente = int(input("Ingrese el exponente en numero positivo: "))

        while contador < exponente:
            resultado*= base
            contador+=1

        if exponente < 0: 
            print("Digite un numero positivo")
        else: 
            resultado = base**exponente
            print(f"{base} elevado a la {exponente} es: {resultado}.")
    elif opcion == 3:
        print("Saliste.")
        break
    else: 
        print("Error")