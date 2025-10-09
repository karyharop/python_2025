print("=" * 40)
print("BUCLES WHILE")
print("=" * 40)

#REPASOOO CON ALAN
# Aquí tambien se pueden hacer archivos .md, para hacer anotaciones

# resumenes

#Formatear cadenas de texto strings para introducir
#datos de variables 

#Con una variable

precio = 55
descripcion = "El producto vale {} euros"

print(descripcion.format(precio))

#Con más de una variable

cantidad = 5
id =34
precio =54
descripcion = "Compra de {} piezas de productos con id {} a precio {}"
print(descripcion.format(cantidad, id, precio))

# Si quiero colocar ddecimales en precio se puede colocar así : precio {:.2f}

# f-string es la forma moderna o rápida de formatear textos:


"""
 de esta forma tambien se puede comentar, es igual que #
    
"""


print(f"Compra de {cantidad} piezas a {precio:.2f} euros")

# > mayor que
# < menor que
# <=menor o igual que
# >= mayor o igual que
# == # aquí se están comparando dos variables
# != # distinto que

# ctrl z es para ir hacia atrás por si borro algo sin querer

# Operadores de membresía para evaluar si un elemento está contenido en otro
# in
# not in
# Se usa habitualmente en string y para listas o estructuras de datos

nombre = "Alan"
nombre_completo = "Alan Sastre"
print(nombre in nombre_completo) # true

nombre = "Pépe"
nombre_completo = "Alan Sastre"
print(nombre in nombre_completo) # false

# JUPITER NOTEBOOK
# CUADERNO PARA EJECUTAR CELDAS DE PYTHON CADA UNA CON SU PROPIO RESULTADO
# IDEAL PARA CIENCIA DE DATOS
# DESDE GOOGLE : COLAB.RESEARCH.GOOGLE.COM, CON EL CORREO SE PUEDE HACER UNA PAGINA

# Lo más basico que se puede hacer con un while, es un
#
# while true (bucle infinito)
contador = 0

while contador < 10:
    print(contador)
    contador += 1 # es igual que decir contador = contador + 1
    
while True:
    print("""
          welcome
          eligeuna opcion:
          1 - Mostrar productos
          2 - Mostrar un producto
          salir - salir del programa
        """)
    
    opcion = input("introduce una opcion: ")
    print(f"Has elegido la opción: {opcion} ")

    if opcion == "salir": opcion = "salir"
    print("Hasta la próxima")
    break # rompe el flujo del bucle

print ("Fuera del bucle")

print("\n")
print("=" * 40)
print("IMPRIME NUMEROS IMPARES")
print("=" * 40)
print("\n")

numero = 0

while numero < 10:
    numero+= 1
    if numero % 2 == 0: # comprobar si el numero es par
        continue # no rompe el bucle, sólo salta a la siguiente interaccion
    print(f"Número impar {numero}")

# Iterar una estructura de datos, por ejemplo lista []
# La f(x) pop viene de las listas, y elimina y devuelve un elemento de la lista
nombres = ["Kary", "Jorge", "Marcos"] # si tiene corchetes es lista

while nombres: nombres = ["Kary"]
# if len(nombres) == 0:
# print("Ya no quedan más nombres, este es el último:")
    nombre = nombres.pop()
    print(nombre)
    
# pass indica que no hay codigo todavia, se suele escribir cuando estamos
# diseñando al principio qué código habrá sin crearlo del todo aún

# Sin pass me obliga a escribir código, ya que no puede estar vacío.




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    















































