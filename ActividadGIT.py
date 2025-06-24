import os
os.system("cls")


def validar_lista_numeros(mensaje):
    while True:
        try:
            lista_numeros = [int(num) for num in input(mensaje).split()]
            
            return lista_numeros
        except ValueError:
            print("Error: Ingrese una lista de números enteros válidos separados por espacios.")


numeros_ingresados = validar_lista_numeros("Ingrese una lista de números enteros separados por espacios: ")

numeros_pares = [num for num in numeros_ingresados if num % 2 == 0]
numeros_impares = [num for num in numeros_ingresados if num % 2 != 0]

print(f"Números pares: {numeros_pares}")
print(f"Números impares: {numeros_impares}")
