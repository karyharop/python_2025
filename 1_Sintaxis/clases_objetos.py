
    """
  Una clase es una plantilla o plano que define:

- Características (atributos): color, precio, raza, altura, id
- Comportamientos (métodos): arrancar, ladrar, iniciar sesión

  
    """

class Coche:
    # definimos atributos y métodos
    pass

mi_coche = coche()
coche_de_amigo = Coche()


"""
constructor: método especial que se ejecuta automáticamente
cuando creamos un nuevo objeto.

El método __init__ se ejecuta automáticamente al crear
el objeto y sirve para dejar el objeto con datos
iniciales.

self -> hace referencia a la variable principal, en el caso del ejemplo 
self, hace referencia a Persona.

    
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        

personal = Persona("Carla", 50) 



class Libro:
    # atributos: titulo, autor, numero páginas
    # métodos: abrir, leer, cerrar, subrayar
    pass
    def __init__(self, titulo, autor, isbn, numero_paginas, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.isbn = isbn
        self.abierto = False # si quieres abrir el libro
        self.pagina_actual = 0 # iniciamos en la pagina 0 (cerrado)
   
# libro_python = Libro()
book = Libro("shag", "Alanna", 1500) 

def abrir(self):
    self.abierto = True
    print(f"Se ha abierto {self.titulo}")

def cerrar(self):
    self.abierto = False
    print(f"Se ha cerrado {self.titulo}")

class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        

# Crear libros
libro1 = Libro("Marianela", "Benito Pérez Galdos", 200, "677854564556544")
libro2 = Libro("El Principito", "Antoine de Saint Exuperi", 180, "57756546456565656", False)

# verificar si está disponibles

print(f"{libro1.titulo} (libro1) está {'Disponible' if libro1.disponible else 'Prestado'}")
print(f"{libro2.titulo} (libro2) está {'Disponible' if libro2.disponible else 'Prestado'}")
   

# Crear objetos Producto
laptop = Producto("Portatil baratucho", 350) # El stock, será 0
# esto debido al valor por defecto que se ha colocado
teclado = Producto("Teclado mecánico", 80, 15)
# ahora es 15, porque se ha especificado

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.perimetro = (ancho + alto) * 2
        
# Crear objeto rectángulo
rectangulo = Rectangulo(5,3)
print(rectangulo.perimetro)

"""
Al definir valores predeterminados para los parámetros del 
constructor los convertimos en opcionales.

"""       
print("\n")
print("VALIDACION_ATRIBUTOS")
print("\n")


class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        
        # Validacion para que el saldo inicial sea como 
        # minimo 0 (no tenga valor -)
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        
        self.saldo = saldo_inicial
        
# Crear objetos cuenta
cuenta_ana = Cuenta("Ana", 1000)

# Esto lanzará un ValueError , el try/except es para controlar un error
try:
    cuenta_problemática = Cuenta("Juan", -500)
except ValueError as e:
    print(f"ERROR: {e}")
    
        
        











































