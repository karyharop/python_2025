# VARIABLES <- SON DATOS CON NOMBRE
# UNA VARIABLE ES UN NOMBRE QUE APUNTA A UN DATO
print("\n")
print("=" * 40)
print("VARIABLES")
print("=" * 40)
print("\n")

edad = 25
nombre = "Jacinta Dorotea"
altura = 1.74
es_estudiante = True

x = y = z
print = (f"variables: x={x}, y={y}, z={z}")
      
nombre, edad, altura = """Jacinta Dorotea""", 25, 1.74
print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}")

print("\n")
print("=" * 20)


a = 5
b = 10
a, b = b, a  # Intercambio de valores

a, b = b, a  # Intercambio de valores
print(f"a: {a}, b: {b}")

print("\n")
print("=" * 20)

contador = 0
print(f"Contador: {contador}")

contador -= 2  # Incrementa el contador en 2
print(f"Contador después de restar 2: {contador}")

precio = 100
precio *= 1.21  # Aplica un aumento del 21%
print(f"Precio: {precio}")

precio /= 2
print(f"precio: {precio}")

edad = 10
Edad = 20
EDAD = 30

# Hay que respetar como se escribe la variable, porque la coge como en este caso 3 
# variables diferentes

print("\n")
print("=" * 20)

#__snake_case <- señala a las variables con guion bajo y minúsculas

#__pascal_case <- señala a las variables con mayúsculas en cada palabra
#como se usa en PseInt
#__camelCase <- señala a las variables con mayúsculas en 
# cada palabra excepto la primera palabra


print("\n")
print("=" * 40)
print("AMBITO LOCAL Y GLOBAL")
print("=" * 40)
print("\n")

mensaje = "Hola MUNDO"

print(mensaje)  # Accede a la variable global

contador_global = 100 # Variable global
print(f"Contador global antes de la función: {contador_global}") #imprime 100

# Def <-- define una función

def incrementar():
    global contador_global  # Indica que se usará la variable global
    contador = 0  # Variable local
    print(f"Contador Local + 1: {contador}")
    contador += 1
    print(f"Contador Local después de incrementar: {contador}")
    
    incrementar() # imprime: "contador local: 1"
    
    print(f"Contador global dentro de la función: {contador_global}") #imprime 100
    
# Siempre que queramos usar una variable global dentro de una función, 
# hay que poner global antes de usarla, si no, la función crea una variable local

# incrementar()  # Llama a la función

# def funcion(): #aqui llama a la funcion, ejemplo (1), si no encuntra la variable, se va a la 
    # fucion siguiente. 
    
    def funcion():
        variable: 1
        def funcion_secundaria():
        print(variable)  
    

print("\n")
print("=" * 40)
print("CONSTANTES")
print("=" * 40)
print("\n")


#LISTA, ESTRUCTURA DE DATOS MODIFICABLES, PUEDES TENER VALORES DUPLICADOS
#mi_lista = [1, 2, 3, 4, 5]
#TUPLAS, ESTRUCTURA DE DATOS NO MODIFICABLES
#mi_tupla = (1, 2, 3, 4, 5)
#CONJUNTOS, ESTRUCTURA DE DATOS NO MODIFICABLES, NO PERMITE VALORES DUPLICADOS
#mi_conjunto = {1, 2, 3, 4, 5}
#ARRAYS, ESTRUCTURA DE DATOS MODIFICABLES, PERMITE VALORES DUPLICADOS, DEBEN SER DATOS DEL MISMO TIPO
# LOS ARRAYS SE USAN MUCHO EN CIENCIA DE DATOS
#mi_array = array.array('i', [1, 2, 3, 4, 5]) # 'i' indica que son enteros
#DICCIONARIOS, ESTRUCTURA DE DATOS MODIFICABLES, PERMITE VALORES DUPLICADOS, SE USAN PARA ALMACENAR PARES DE VALOR-CLAVE
#mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2'}, TAMBIEN LLAMADOS SETS DE DATOS
#LOS DICCIONARIOS SON MUY USADOS EN PROGRAMACION WEB, PARA ALMACENAR DATOS DE USUARIOS

print("\n")
print("=" * 40)

PI = 3.14159  # Constante matemática
VELOCIDAD_LUZ = 299792458  # en metros por segundo
GRAVEDAD_TIERRA = 9.81  # en m/s^2
DIAS_SEMANA = 7  # Días en una semana
USER_DEFAULT = "Usuario"

# Si qiueres mantener las constantes, debes añadirlas en un archivo aparte
# y llamarlas desde ahí, para que no se modifiquen

print("\n")
print("=" * 40)
print("OPERADORES ARITMÉTICOS")
print("=" * 40)
print("\n")

precio_manzanas = 3
precio_naranjas = 4
total_frutas = precio_manzanas + precio_naranjas
print(f"Total de la compra: {total_frutas} euros")

dinero_entregado = 20
dinero_producto = 13
cambio = dinero_entregado - dinero_producto
print(f"Su cambio es: {cambio} euros")

precio_unitario = 5
cantidad = 3
precio_total = precio_unitario * cantidad
print(f"Precio por {cantidad} unidades: {precio_total} euros")
precio_total /= 2  # Aplica un descuento del 50%

pizza = 8 / 2
print(f"8 / 2 = {pizza}")

horas_totales = 90
horas_por_dia = 24
dias_completos = horas_totales // horas_por_dia
print(f"Días completos en 90 horas: {dias_completos} días")

horas restantes = horas_totales % horas_por_dia
print(f"Horas restantes después de días completos: {horas_restantes} horas")
print("\n")
print("=" * 40)

lado = 4
area_cuadrado = lado ** 2
print(f"Área del cuadrado es: {area_cuadrado} unidades cuadradas")

numero = 27
raiz_cubica = numero ** (1/3)
print(f"La raíz cúbica de {numero} es: {raiz_cubica}")

print("=" * 40)

resultado = 0.2 + 0.1
it  (f"El resultado de 0.2 + 0.1 es: {resultado}")
#me falta escribir print(resultado)

print("\n")
print("=" * 40)
print("OPERADORES EN COMPARACION")
print("=" * 40)
print("\n")


precio_producto_a = 15
precio producto_b = 10

es_mas_barato_ = precio_producto_b < precio_producto_a
print(f"¿El producto B es más barato que el A? {es_mas_barato}")

print("\n")
print("=" * 40)
print("OPERADORES LÓGICOS")# SON PARA EVALUAR OPERACIONES BOOLEANAS
print("=" * 40)
print("\n")

NOT # NEGACION
AND # Y
OR  # O, es más permisivo que el AND
XOR # O EXCLUSIVO

print("\n")
print("=" * 40)

ingresos_suficientes = True
buen_historial_crediticio = True

aprobacion_prestamo = ingresos_suficientes and buen_historial_crediticio
print(f"¿El préstamo fue aprobado? {aprobacion_prestamo}")

es_socio = False
tiene_invitacion = True

puedo_entrar_evento = es_socio or tiene_invitacion
print(f"¿Puedo entrar al evento? {puedo_entrar_evento}")

disponible = False
no_disponible = not disponible


