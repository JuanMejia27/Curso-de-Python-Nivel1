
a = 5 + 9
print("La suma de 5 y 9 es:", a)

b = 7
c = 15
d = b + c #Suma entre variables
print("La suma de", b, "y", c, "es:", d)

e = 20/3 #Division simple
print("La division de 20 entre 3 es:", e)

f = 73/5 #Division simple
print("La division de 73 entre 5 es:", f)

g = b - c - (e - c) #Resta con operaciones anidadas entre varuables
print("La resta de", b, "y", c, "es:", g)

h = b//c #Division entera la cual devuelve el cociente sin decimales
print("La division entera de", b, "entre", c, "es:", h)

i = b%c #Modulo el cual devuelve el residuo de la division
j = 7%2
print("El residuo de", b, "entre", c, "es:", i)
print("El residuo de 7 entre 2 es:", j)

#prioridad de operaciones o jerarquia de operaciones
k = 5 + 3 * 2 #Se realiza primero la multiplicacion y luego la suma
l = (5 + 3) * (2 * 8)/8 #Se realiza primero la suma y luego la multiplicacion
print("El resultado de la expresion 5 + 3 * 2 es:", k)
print("El resultado de la expresion (5 + 3) * (2 * 8)/8 es:", l)

res = 7**5 + (15/3) #Potencia y division por jerarquia de operaciones se realiza primero los parentesis con la division y luego la potencia
print("El resultado de la expresion 7**5 + (15/3) es:", res)