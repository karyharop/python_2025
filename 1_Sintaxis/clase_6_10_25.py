print("\n")
print("=" * 40)
print("ESTRUCTURAS CONTROL CONDICONAL")
print("=" * 40)
print("\n")

print("\n")
print("=" * 40)
print("IF")
print("=" * 40)
print("\n")

# Estructura if, si se cumple la condición, se ejecuta el bloque de código indentado
# Si no se cumple, se salta el bloque de código indentado

edadMayor = 20
    print(f"Tienes {edadMayor} años")

if edad >=18:
    print("Eres mayor de edad")
    
edad = 18
print (f"Tienes {edad} años")

hora = 10
print(f"Hora: {hora}")

if hora >=6 and hora < 12:
    print("Buenos días")
    
    #horas que cumplen esta condicion: 6, 7, 8, 9, 10, 11
    
    numero = 15
    print(f"Número: {numero}")
    
    if numero == 15:
        print("== El número es igual a 15")
    
    if numero ! = 10:
        print("!= El número es distinto a 10")
        
    if numero > 10:
        print("> El número es mayor a 10")
        
    if numero < 20:
        print("< El número es menor a 20")
        
    if numero >= 15:
        print(">= El número es mayor o igual a 15")
        
    if numero <= 20:
        print("<= El número es menor o igual a 20")
        
        # operadores de comparación
        # En un if, siempre cerrar con un else
        
    print("\n")
print("=" * 40)
print("IF - ELSE")
print("=" * 40)
print("\n")    
        
edad = 17
print(f"Edad {edad} años") 

if edad >= 18:
    print("Puedes votar en las elecciones") 
else:
    print("No puedes votar en las elecciones")
    
numero = 15
print(f"Número: {numero}")

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
    
    
print("\n")
print("=" * 40)
print("IF - ELIF - ELSE")
print("=" * 40)
print("\n")

numero = 0
print(f"Número: {numero}")

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
 
 numero = 8
print(f"Número: {numero}")
    
print("\n")
print("=" * 40)
print("MATCH - CASE")
print("=" * 40)
print("\n")

fruta = input("introduce una fruta: ")

match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "plátano":
        print("La fruta es un plátano.")
    case _: #la barra baja es como el else
        print("Fruta desconocida.")
        
print("\n")

punto = (0, 0)# hay que ir definiendo coordenadas x e y

match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (x, 0):
        print(f"El punto está sobre el eje X en la coordenada {x}.")
    case (0, y):
        print(f"El punto está sobre el eje Y en la coordenada {y}.")
    case (x, y):
        print(f"El punto está en la coordenada x={x}, y={y}).")
    case _:
        print("No es un punto válido.")

edad = 20
print(f"Tienes {edad} años")

match edad:
    case edad if edad < 18:
        print("Eres menor de edad.")
    case edad if edad == 18:
        print("Tienes 18 años, eres mayor de edad.")
    case edad if edad > 18 and edad < 65:
        print("Eres un adulto.")
    case edad if edad >= 65:
        print("Eres un adulto mayor.")
        
print("\n")
print("=" * 40)
print("CONDICIONALES ANIDADOS")
print("=" * 40)
print("\n")

edad = 30 
estado_civil = "soltero"
print(f"Edad: {edad}, estado civil: {estado_civil}")

if edad >= 18:
    if estado_civil == "casado":
    print("Eres un adulto casado")
    else:
    print("Eres un adulto soltero.")
else:
    print("Eres menor de edad.") 
    
   print("\n")
print("=" * 40)
print("CONDICIONAL TERNARIO")
print("=" * 40)
print("\n")    
    
edad = 17
print(f"Edad: {edad}")

mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad"

print(mensaje)

print("\n")
print("=" * 40)
print("ESTRUCTURAS_CONTROL_ITERATIVO")
print("=" * 40)
print("\n")


print("=" * 40)
print("BUCLE FOR")
print("=" * 40)

frutas = ["manzana", "plátanos", "cerezas"]
print(f"Lista de frutas: {frutas}")

# Para cada elemento de la lista frutas... o puede ser Para cada fruta en frutas.

for elemento_de_lista in frutas:
    print(elemento_de_lista)
    
 
print("=" * 40)
print("RANGE")
print("=" * 40)   

for i in range (5):# en Python, este rango comienza en 0.
    #en PseInt, comenzaba en 1
    print(i)

# ejemplo
for i in range (3,8):
    print(i)
 
for i in range (2, 11, 2):
    print(i)
     
     #ejemplo

for i in range (5, 0, 1):
    print(i)
     

print("=" * 40)
print("ITERAR_SOBRE_ÍNDICES")
print("=" * 40)

nombres : ["Ana", "Carlos", "Elena"]
print(f"Lista de nombres: {nombres}")

for i in range(len(nombres)):
    print(f"Posicion {i}: {nombres[i]}")
    
# Tambien se puede hacer así... es igual    
for indice, nombre in enumerate(nombres):
    print(f"Posicion {indice}: {nombre}")























































































   
    





