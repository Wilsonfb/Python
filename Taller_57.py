#57.  Programa que permita calcular la cantidad total de clientes que atienden en un mes un hotel utilizando un vector. Como entrada se debe solicitar el número de clientes que atiende el hotel cada día del mes.

mes = []

i = 0 

while i < 30:
    clientes = int(input(f"Cantidad de clientes que ingresaron {i+1}: "))
    i+=1
    mes.append(clientes)

print(mes)

total_cli = sum(mes)

print(f"El mes entraron {total_cli} clientes.")
