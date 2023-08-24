
def sum(x, y):
    return x+y


def login(username, password):
    if((username == "username") and (password == "password")):
        return True
    else:
        return False
    

def cambio(articulo, dinero_entregado):
    if articulo > dinero_entregado:
        return articulo - dinero_entregado
    elif articulo < dinero_entregado:
        return articulo - dinero_entregado
    else:
        return 0


def holaMundo():
    return "¡Hola, mundo!"

def numPI(num1, num2):
    pares = []
    impares = []
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            impares.append(i)
        else:
            pares.append(i)
    return [impares, pares]


def countLengt(frase):
    palabras = frase.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras


def numPrimos(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def genFibonacci(n):
    serie = [0, 1]
    while len(serie) < n:
        siguiente = serie[-1] + serie[-2]
        serie.append(siguiente)
    return serie


# Título: Crea un juego donde el programa elige un número aleatorio y el jugador debe adivinarlo.

# import random
# n = random.randint(1, 100)

def adivinaNumeroRandom(n):
    intentos = 0
    while True:
        intentos += 1
        adivinado = int(input('Intento {}: Adivina el numero: '.format(intentos)))

        if adivinado == n:
            print("¡Correcto! Lo adivinaste en {} intentos.".format(intentos))
            break
        elif adivinado < n:
            print("El número es más grande.")
        else:
            print("El número es más pequeño.")


# resultado = adivinaNumeroRandom(n)
# print(resultado)


# Título: Cuenta la cantidad de veces que aparece cada letra en una frase ingresada por el usuario.

def contadorLetras(frase):
    contador_letras = {}
    for letra in frase:
        if letra.isalpha():
            if letra in contador_letras:
                contador_letras[letra] += 1
            else:
                contador_letras[letra] = 1
    
    for letra, cantidad in contador_letras.items():
        print("La letra '{}' aparecio {} veces".format(letra, cantidad))

# contadorLetras('Hola que tal')

# Título: Crea un programa que convierta entre diferentes unidades (por ejemplo, Celsius a Fahrenheit).


def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def conversor(temperatura, unidad):
    if unidad == "C":
        temperatura_convertida = celsius_a_fahrenheit(temperatura)
        print("La temperatura en Fahrenheit es:", temperatura_convertida)
    elif unidad == "F":
        temperatura_convertida = fahrenheit_a_celsius(temperatura)
        print("La temperatura en Celsius es:", temperatura_convertida)
    else:
        print("Unidad inválida.")
    

# temperatura = float(input("Ingrese la temperatura: "))
# unidad = input("Ingrese la unidad (C/F): ")

# Título: Crea un juego donde el programa elige una palabra y el jugador debe adivinarla, mostrando progresivamente más letras.
import random

def juego_palabras():
    palabras = ["python", "programacion", "computadora", "desafio"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []

    while True:
        progreso = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                progreso += letra
            else:
                progreso += "_"
        print("Palabra:", progreso)

        if progreso == palabra_secreta:
            print("¡Ganaste! La palabra era:", palabra_secreta)
            break

        adivinanza = input("Adivina una letra: ")
        letras_adivinadas.append(adivinanza)

# juego_palabras()

# Título: Escribe una función que sume dos matrices y devuelve el resultado.

def suma_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    suma = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            suma_elemento = matriz1[i][j] + matriz2[i][j]
            fila.append(suma_elemento)
        suma.append(fila)

    return suma

# matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# resultado = suma_matrices(matriz1, matriz2)
# for fila in resultado:
#     print(fila)








