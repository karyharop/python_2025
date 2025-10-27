# Solicitar al usuario la altura del triángulo

altura_triangulo = input("señala la altura del triangulo: ")

# Convertir la entrada a número entero
altura = int(altura_triangulo)


print(f"\nGenerando patrón triangular de altura {altura}: ")
print("-" * 30)

# Generar el patrón usando bucles for anidados
# Bucle externo: para cada fila (desde 1 hasta la altura)
for i in range(1, altura + 1):
    
    # Bucle interno: para cada número en la fila actual (desde 1 hasta el número de fila)
    for numero in range(1, i + 1):

     # Imprimir cada número seguido de un espacio (sin salto de línea)
        print(numero, end=" ")

    # Después de completar una fila, hacer un salto de línea
    print("\n")

print("-" * 30)
print("Patrón completado!")