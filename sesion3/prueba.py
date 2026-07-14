edad = 25
nombre = "Juan"
val1 = 10
val2 = 20
suma = val1 + val2
print("La suma de", val1, "y", val2, "es:", suma)

if edad >= 18:
    print(nombre, "es mayor de edad.")
else:
    print(nombre, "es menor de edad.")

validacion = True
invalidacion = False

if edad >= 18 and validacion:
    print(nombre, "es mayor de edad y la validación es verdadera.")
else:
    print(nombre, "es menor de edad o la validación es falsa.")
if edad < 18 or invalidacion:
    print(nombre, "es menor de edad o la validación es falsa.")

num = 17 
num -= 2
print(num)
num *= 3
print(num)
num //= 4
print(num)


'''edad_1 = 0

Edad = 18
edad = 20

a,b,c = 0
a, b, c = 0, 1, 2

#ciclos como For, if, while, asi como funciones, clases, etc. son sensibles a mayusculas y minusculas y los comentarios se agregan con gato en una solo linea, o con triple comillas para varias lineas.

e = 2+5j #tipo de dato complejo, se puede usar j o J para denotar la parte imaginaria.
z = "Hola"
t = "Mundo"
#se pueden realizar operaciones aritmeticas como suma, resta, multiplicacion, division, potencia, etc. con los tipos de datos numericos y de forma directa como 2*5 2+9 9-8 etc.
u = (5+6)*(2/8)-10
# doble // para division entera, % para modulo, ** para potencia
r = 10//3
s = 10%3
t = 10**3
#operadores de comparacion como ==, !=, >, <, >=, <=
v = 5 == 5
w = 5 != 5
x = 5 > 5
y = 5 < 5
z = 5 >= 5
#operadores logicos como and, or, not
f = True
g = False
h = not a
i = a and b
j>5 or k<7 and not(l == 9)
#Operadores de asignacion como =, +=, -=, *=, /=, //=, %=, **=
m += 5 #muestra el valor de m y le suma 5
m -= 2 #muestra el valor de m y le resta 2
m *= 3 #muestra el valor de m y le multiplica por 3
m /= 4 #muestra el valor de m y le divide por 4
m //= 5 #muestra el valor de m y le realiza una división entera por 5
m %= 6 #muestra el valor de m y le calcula el módulo por 6'''