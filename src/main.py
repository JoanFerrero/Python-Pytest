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