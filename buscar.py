def buscar_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Ejemplo de uso
lista = [10, 20, 30, 40]
print(buscar_elemento(lista, 30))
