print("\n")
print("=" * 40)
print("funciones practicas")
print("=" * 40)
print("\n")

# Funciones que devuelven números

# Funciones que devuelven un precio con IVA
"""
def calcular_iva(precio):
    
        calcula el IVA a partir de un precio. 
        devuelve el 21% de ese precio
   
    
    
    return precio * 0.21

"""
# Calcula el promedio de una lista de números.
# strip = permite borrar espacios extras 
# Suma todos los números de la lista y divide el resultado
# entre la cantidad de elementos.

# Args:
# numeros: Una lista de valores numéricos

# Returns:
# El promedio como valor flotante

# Ejemplo:
# >>> calcular_promedio([1, 2, 3, 4])
# 2.5

def calcular_iva(precio):
    return precio * 0.21

product_price = 100
calcular_iva(product_price)

# --- explicacion Alan ---

# funciones que devuelven números

# función que devuelve un precio con IVA

def calcular_iva(precio):
    """
    Calcula el IVA de un precio dado.

    Obtiene el 21 % de un precio.

    Args:
    precio: precio mayor que cero

    Returns:
    El IVA en punto flotante (float)

    Ejemplo:
    >>> calcular_iva(100)
    21

    """
    return precio * 0.21


microfono_precio = 100
microfono_precio_iva = calcular_iva(microfono_precio)
print(f"precio original: {microfono_precio}")
print(f"precio con IVA: {microfono_precio_iva}")

# OTRA FORMA

microfono_precio = 100
microfono_iva = calcular_iva(microfono_precio)
print(f"precio original: {microfono_precio}")
print(f"IVA del producto: {microfono_iva}")

print(f"Precio final: {microfono_precio + microfono_iva}")

# crear una f(x) que reciba un numero de inicio y un numero de fin
# Y devuelva una lista con numeros: [inicio, 2, 3, 4, 5, 6 ... fin]
# Lista: usar range()

def crear_lista_numeros(inicio, fin):
    return list(range(inicio, fin))

    
    
lista1 = crear_lista_numeros(1, 5)
print(lista1) # [1, 2, 3, 4, 5]

lista2 = crear_lista_numeros(1, 10)
print(lista2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista3 = crear_lista_numeros(5, 20)
print(lista3) # [5, hasta el 20]


print("\n")
print("=" * 40)
print("F(X)s LOGIN")
print("=" * 40)
print("\n")

def login(email, password):
    email_valido = "admin@gmail.com"
    password_valida = "1234"
    
# Verificar siel mail y el passwoed coinciden

if email == email_valido:
    return True
else:
    return False



login("admin@gmail.com", "abcd1234") # False

login("admin@gmail.com", "1234") # True

login("usuario@gmail.com", "1234") # False

# Un ejemplo

if login("admin@gmail.com", "1234"):
    pass


# LOGIN CON NÚMERO MÁXIMO DE INTENTOS

# Aquí podemos crear una aplicación de consola
# que pida al usuario email y password,
# si falla tres veces detiene el programa y no deja continuar
# si acierta le deja usar la aplicación

valid_email = "Anna@gmail.com"
valid_password = "A_12"
max_intentos = 3

def login1(valid_email, valid_password):
# bucle for para máximo 3 intentos fallidos para verificar mail y contraseña
# leer por input el email y password
    for intento in range (1, max_intentos + 1) # 1, 2, 3,
    email = input("introduce email: "). strip()
    password = input("Introduce password: "). strip()
    
    if email == valid_email and password == valid_password
        return True
    
    intentos_restantes = max_intentos - intento # 3 - 1 = 2, 3 - 2 = 1, 3 - 3 = 0
    if intentos_restantes > 0:
        print(f"Credenciales incorrectas, te quedan {intentos_restantes} intentos")
    else:
        print("Has agotado todos los intentos, adiós.")
        sys.exit(1) # corta de forma definitiva el programa


if login():
    opcion = elegir_opcion()
    
    
def login_2():
    pass

def elegir_opcion():
    print("")
opcion = input()
    return opcion


    if login_1():
        opcion = elegir_opcion()
        print(f"Has elegido la opcion {opcion}")
# hacer algo en base a la opcion elegida por el usuario:    
# hacer algo en base a la opcion elegida por el usuario:
# if...
# elif...
# elif...
# else

if login_1():
    while True:
    print("Bienvenido/a a la aplicación. Opciones disponibles: 1 - ver productos, 2 - crear producto, 3 - terminar el programa.")
opcion = input("Introduce una opción: ")
print(f"Has elegido la opcion {opcion}")

if opcion == "1":
    print("1")
elif opcion == "2":
    print("2")
elif opcion == "3" or opcion == "salir":
    print("saliendo...")
    break
else:
    print("opción incorrecta.")
    

print("\n")
print("=" * 40)
print("LISTAS")
print("=" * 40)
print("\n")

"""
Listas: [] o list()

* mutables: se pueden modificar, reordenar, añadir elementos, borrar

Métodos relevantes:

* Longitud: len()

CRUD: (Create, Read, Update, Delete)

* Acceso elementos:
    * Primero: nombres[0]
    * Último: nombres[-1]
    * IndexError: list index out of range si ponemos un índice fuera del rango

* Slicing:
    * nombres[1:4]
* Mutar un elemento mediante asignacion:
    * precios[0] = precios[0] * 1.21
    
    
* Añadir o combinar:
    * nombres.append("Patricia")
    * nombres.extend(['n1', 'n2'])
    * nombres.insert(index, 'Bob')

* Eliminar elementos:
    * pop() quita y devuelve el último elemento
    * pop(0) quita y devuelve el primer elemento
    * remove(x) elimina la primera ocurrencia del nombres[0]
    * nombres.clear()
    
* Recorrer:
    * for nombre in nombres: print()
    * for index, nombre in enumerate(nombres): print(f"Índice: {index}, nombre {nombre}")
    * for index in range(len(nombres1)): print(nombres1[index])
    
* Buscar:
    * 'Pepe' in nombres
    * nombres.index('María') devuelve el indica de la primera ocurrencia    

"""

nombres1 = ['Juan', 'María', 'Mike', 'Pepe', 'Reyes', 'Kary']
nombres2 = ['Juan', 'María', 'Mike', 'Pepe', 'Reyes', 'Kary']

print(nombres1 + nombres2)



            






















