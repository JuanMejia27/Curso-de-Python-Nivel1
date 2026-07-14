import math #importamos la libreria math para poder utilizar funciones matematicas

raiz = math.sqrt(25) #raiz cuadrada de 25
print("La raiz cuadrada de 25 es:", raiz)
raiz2 = math.sqrt(17) #raiz cuadrada de 17
print("La raiz cuadrada de 17 es:", raiz2)
redo = math.ceil(raiz2) #redondeo hacia arriba de la raiz cuadrada de 17
print("El redondeo hacia arriba de la raiz cuadrada de 17 es:", redo)
redo2 = math.floor(raiz2) #redondeo hacia abajo de la raiz cuadrada de 17
print("El redondeo hacia abajo de la raiz cuadrada de 17 es:", redo2)

sen = math.sin(math.radians(30)) #seno de 30 grados
print("El seno de 30 grados es:", sen)
sen2 = math.floor(math.sin(math.radians(45))) #seno de 45 grados
print("El seno de 45 grados es:", sen2)

cos = math.cos(math.radians(30)) #coseno de 30 grados
print("El coseno de 30 grados es:", cos)

tan = math.tan(math.radians(30)) #tangente de 30 grados
print("La tangente de 30 grados es:", tan)

log = math.ceil(math.log(10)) #logaritmo de 10
print("El logaritmo de 10 es:", log)
#------------------------------------------------------------------

radio = 5
area = math.pi * radio**2 #Area de un circulo con uso de la constante pi de la libreria math
print("El area de un circulo con radio 5 es:", area)
arearedo = math.floor(area) #redondeo hacia abajo del area del circulo
arearedo2 = math.ceil(area) #redondeo hacia arriba del area del circulo
print("El redondeo hacia arriba del area del circulo es:", arearedo2)
print("El redondeo hacia abajo del area del circulo es:", arearedo)

op = (5+3)**2//3-4 #operacion con jerarquia de operaciones, primero se realiza la suma, luego la potencia, despues la division y por ultimo la resta
print("El resultado de la operacion (5+3)**2//3-4 es:", op)

