
lineas = 5


for numero_linea in range(lineas):
    espacios = lineas - numero_linea - 1
    asteriscos = 1 + numero_linea * 2
    print (" " * espacios + "*" * asteriscos)