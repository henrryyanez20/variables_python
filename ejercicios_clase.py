#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para poner a prueba los conocimientos adquiridos durante la clase
'''

__author__ = "Coding School"
__email__ = "henrryyanez@"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica numérica
    
    # Operadores con números decimales
    print('Ingrese el primer número decimal a operar:')
    numero_1 = int(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = int(input())
    
    # Alumno: Imprima en pantalla los dos números decimales solicitados
    print(" [*] Primer valor ingresado :",numero_1,"\n","[*]Segundo valor ingresado :",numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    suma = numero_1 + numero_2
    # Resta
    resta = numero_1 - numero_2

    # División
    dividir = numero_1 / numero_2
    # Multiplicación
    muliplicar = numero_1 * numero_2

    print("\n El resultado de sumar",numero_1,"con",numero_2,"es:",suma)
    print("\n El resultado de restar",numero_1,"con",numero_2,"es:",resta)
    print("\n El resultado de dividir",numero_1,"con",numero_2,"es:",dividir)
    print("\n El resultado de multiplicar",numero_1,"con",numero_2,"es:",muliplicar)


def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números reales
    print('Ingrese el primer número real a operar:')
    numero_3 = float(input())

    print('Ingrese el segundo número real a operar:')
    numero_4 = float(input())

    # Alumno: Imprima en pantalla los dos números reales solicitados
    print(" [*] Primer valor ingresado :",numero_3,"\n","[*]Segundo valor ingresado :",numero_4)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_3, numero_4
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    suma2 = numero_3 + numero_4
    # Resta
    resta2 = numero_3 - numero_4

    # División
    dividir2 = numero_3 / numero_4
    # Multiplicación
    muliplicar2 = numero_3 * numero_4

    print("\n El resultado de sumar",numero_3,"con",numero_4,"es:",suma2)
    print("\n El resultado de restar",numero_3,"con",numero_4,"es:",resta2)
    print("\n El resultado de dividir",numero_3,"con",numero_4,"es:",dividir2)
    print("\n El resultado de multiplicar",numero_3,"con",numero_4,"es:",muliplicar2)


#def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo

    nombre_completo = nombre+" "+apellido
    print("[*] Tu nombre completo es:",nombre_completo)

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....

    # Imprimir la cantidad de letras que posee su nombre completo
    letras_cantidad=len(nombre_completo)
    print("[*] El nombre que ingresaste está compuesto de",letras_cantidad,"caracteres")
def ej3():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla

    print("El acrónimo de las palabras("+palabra_1+","+palabra_2+","+palabra_3+") que introduciste es: "+"\n[*] Acrónimo: "+palabra_1[0]+palabra_2[0]+palabra_3[0])

def ej4():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    # Imprima en pantalla los resultados

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    ej3()
    #ej4()
