#EJERCICIOS CON LAMBDA (25 puntos) - Examen Final Libres PROGRAMACIÓN II (Mesa de Agosto)

# Realizar una función lambda que eleve al cuadrado un número pasado como parámetro
# (Nota 1: la lambda debe estar "in line", es decir, directamente dentro del map)
# (Nota 2: no debe usarse una función llamada "potencia_2", sino la lambda directamente)

# Lista de números a procesar
números = [1, 2, 3, 4, 5]

# Aplicamos map con una lambda que eleva cada número al cuadrado
resultados = list(map(lambda x: x ** 2, números))

# Mostramos la nueva lista con los resultados (potencias al cuadrado de cada número)
print(resultados)
