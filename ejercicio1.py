lista =[2, 3, 6, 8, 10, 9]
"""""//prueba= lista[2:6]
//print(prueba)"""
def rotacion_circular(lista, n, direccion):
    if len(lista)==0:
        return lista
    n = n % len(lista)
    if direccion == "derecha":
        return rotacion_circular(lista[:-n], n, lista[-n:])
    elif direccion == "izquierda":
        return rotacion_circular(lista[:n], n, lista[n:])
    else:
        print("pon ""izquierda""O" "derecha")
        return lista
print("original:", lista )
print(rotacion_circular(lista, 2, "izquierda"))
print(rotacion_circular(lista, 2, "derecha"))
