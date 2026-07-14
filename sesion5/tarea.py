import math

# Area de un rectangulo, alto=8, ancho=4.5, resultado con redondeo hacia rriba y hacia abajo
alto = 8
base = 4.5

area = alto * base
perimetro = 2 * (alto + base)

redo_arriba = math.ceil(area)
redo_abajo = math.floor(area)
per_arriba = math.ceil(perimetro)
per_abajo = math.floor(perimetro)

print("El area del rectangulo es:", area)
print("El perimetro del rectangulo es:", perimetro)
print("El redondeo hacia arriba del area del rectangulo es:", redo_arriba)
print("El redondeo hacia abajo del area del rectangulo es:", redo_abajo)
print("El redondeo hacia arriba del perimetro del rectangulo es:", per_arriba)
print("El redondeo hacia abajo del perimetro del rectangulo es:", per_abajo)
