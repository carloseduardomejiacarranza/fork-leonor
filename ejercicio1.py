lista =[2, 3, 6, 8, 10, 9]

def rotacion_circular(lista, n, direccion):
    if len(lista)==0:
        return lista
    n = n % len(lista)
    if direccion == "right":
        return rotacion_circular(lista[:-n], n, lista[-n:])
    elif direccion == "left":
        return rotacion_circular(lista[:n], n, lista[n:])
    else:
        print("pon ""left" "O" "right")
        return lista

print("original:", lista )

print(rotacion_circular(lista, 2, "left"))

print(rotacion_circular(lista, 2, "right"))


"solo corrijo el idioma"
