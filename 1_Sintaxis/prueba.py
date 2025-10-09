# Para aprender...
print("¡Hola, mundo!")
# comentario

# ejemplos clases
# print es el escribir de PseInt
edad = 25
temperatura_bajo_cero = -10
poblacion_mundial = 8.000.000.000


# print("\n") <- es un salto de linea


print(f"edad: {Edad}")
print("Edad: " + str(edad))
print(f"Temperatura_bajo_cero: {temperatura_bajo_cero}")
print(f"Poblacion_mundial: {poblacion_mundial}")

numero_grande = 12345567744645656757345
print(f"numero_grande: {numero_grande}")
print(f"numero_grande + 1: {numero_grande + 1}")

print("NUMEROS DECIMALES (FLOAT)")


suma = 5 + 3
resta = 10 - 4
multiplicacion = 3 * 7
division = 20 / 4

#Asignación con valores predeterminados
#Podemos usar el operador de asignación con el método get() (no lo entiendo bien)

print(f""suma: {suma}")
print(f"resta: {resta}")
print(f"multiplicacion: {multiplicacion}")
print(f"division: {division}")
print(f"division entera: {20 // 3}")

complejo = 3 + 4j
print(f"complejo: {complejo}")
print(f"parte real: {complejo.real}")
print(f"parte imaginaria: {complejo.imag}")

redondeo_decimal = round(3.14159, 2)
print(f"redondeo a 2 decimales: {redondeo_decimal}")
print(f"redondeo a 3 decimales: {round(3.14159, 3)}")

# conversion 
# f = convierte inmediatamente a entero, format
edad_aproximada = int(27.3) #si colocas int, redondea hacia abajo
print(f"edad_aproximada: {edad_aproximada}")
precio_exacto = float(20) #si colocas float, agrega .0
print(f"precio_exacto: {precio_exacto}")

import random

dado = random.randint(1, 6) #genera un numero aleatorio entre 1 y 6

print(f"Tirar un dado: {dado}")
print(f"Tirar un dado: {random.randint(1, 6)}")
print(f"Tirar un dado: {random.randint(1, 4)}")
print(f"Tirar un dado: {random.randint(1, 10)}")
print(f"Tirar un dado: {random.randint(1, 12)}")
print(f"Tirar un dado: {random.randint(1, 20)}")

print("\n")
print("TEXTO (STRING)")
print("\n")

nombre_simple = "Kary"
mensaje = "Hola, ¿Cómo estás?"
descripcion = '''Este es un texto # estas 3 comillas simples permiten que la frase se repita en varias líneas sin problema.

print(nombre_simple)
print(mensaje)
print(descripcion)'''

print("=" * 40) #multiplica el string 40 veces =======, o con 20, metodo de cadena

# ejemplo

genero = Corvus
especie = Monedula
especie_minuscula = especie.lower() #minuscula

nombre_cientifico = genero + "" + especie_minuscula
print(f"Nombre cientifico: {nombre_cientifico}")

print("=" * 40)

# tabulacion es \t
# salto de linea es \n
print("primera_linea\nsegunda_linea\ntercera_linea")

edad = 25
edad_texto = str(edad) #convierte a texto
print("Edad: " + edad_texto)


print("\n")
print("=" * 20)
print("BOOLEAN")
print("=" * 20)
print("\n")

esta_lloviendo = True
print(f"¿Está lloviendo? {esta_lloviendo}")

es_fin_de_semana = False
print(f"¿Es fin de semana? {es_fin_de_semana}")

print("\n")
print("=" * 20)
print("CONVERSIONES")
print("=" * 20)
print("\n")

print(bool(0)) #True
print(bool(42)) #False
print(bool("")) #False
print(bool("Hola")) #True
print(bool([])) #False
print(bool([1, 2, 3])) #True

#tupla, es una estructura de datos invariable, despues e ser creada, no puede cambiarse
# ejemplo, la tupla 1,2,3. Se suele usar con datos que no van a cambiar. ejemplo, coordenadas
#  listas con corchetes, tuplas con parentesis, diccionarios con llaves =)

print("\n")
print("=" * 20)
print("CONVERSIONES")
print("=" * 20)
print("\n")




















































