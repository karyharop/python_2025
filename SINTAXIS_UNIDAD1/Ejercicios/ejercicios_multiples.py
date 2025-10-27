print("=== FUNCIONES===")
"""
Escribe una función que reciba el radio de un círculo y devuelva su área. 
Usa la fórmula: Area= pi * r2   
        
"""
radio = 4
PI = 3.14159
area = PI * radio ** 2

def area_circulo(radio):
    return area

print(f"El área del círculo con radio: {radio}, es: {area}")


"""
Ejercicio 5: CONTAR VOCALES EN UNA CADENA
    
- Crea una funcion que reciba una cadena de texto y cuente
cúantas vocales contiene   
       
"""
def conteo_vocales(cadena):
    vocales = "AEIOUaeiou"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

name = "Kary Haro Perez"
print(f"el texto name contiene {conteo_vocales(name)} vocales.")

"""
6.- NUMERO MAYOR DE UNA LISTA

Escribe una función que reciba una lista de números y devuelva el numero mayor. 
      
"""
def numero_mayor(lista):
    return max(lista)

numeros = 10, 13, 25, 45, 60, 33, 20
print(f"El número mayor de la lista es: {numero_mayor(numeros)}")

"""
7.- INVERTIR UNA CADENA

Crea una función que reciba una cadena y devuelva la cadena invertida   

lista = [0, 1, 2, 3, 4, 5, 6]
print(lista[::2])  # [0, 2, 4, 6] (toma cada 2 elementos)
ESO SIGNIFICAN LOS ::     SONRISAS =)

    
"""
def cadena_invertida(cadena):
    return cadena[::-1]

# Ejempl uso:

texto = "AMOR"
print(f"La cadena invertida es: {cadena_invertida(texto)}")


"""
8.- COMPROBAR SI UN NUMERO ES PRIMO

Escribe una función que determine si un numero es primo.

"""
def numero_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % 1 == 0:
            return False
        return True
    
# Ejemplo de uso:

numero = 17

if numero_primo(numero):
    print(f"{numero}, es un numero primo")
else:
    print(f"{numero}, no es un numero primo")
    

"""
9.- GENERA UNA TABLA DE MULTIPLICAR

Crea una función que reciba un numero y genere su tabla de multiplicar del 1 al 10. 

"""

def tabla_multiplicar(numero):
    for i in range(1, 13):
        print(f"{numero} x {i} = {numero * i}")
        
#Ejemplo uso:

numero = 8
tabla_multiplicar(numero)
     
