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
