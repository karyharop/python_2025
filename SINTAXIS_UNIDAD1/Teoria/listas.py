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
    * nombres.append("Patricia") la tuve mala en el examen...
    debo recordarla muy bien.
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

