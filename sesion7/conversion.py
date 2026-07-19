
'''edad = input("Ingrese su edad: ") #La entrada de datos es una cadena (string)
edad_int = int(edad) #Convertir la cadena a un número entero
print("Su edad en años es:", edad_int, edad) #Imprimir la edad como número entero'''

'''a = input("Ingrese un numero: ") #Input devuelve un string desde la consola
b = input("Ingrese otro numero: ")
#c = a + b  sumaria los strings, no los números
c = int(a) + int(b) #Convertir los strings a enteros y sumarlos
print(c)'''

#Ejemplo
resultado = 5 + 7.3
print(resultado) #El resultado es un número decimal (float)

#conversion a entero
print(int("17")) #Convertir un string a un número entero
print(int(7.9)) #Convertir un número decimal a un número entero (trunca la parte decimal)
#print(int("hola")) #No se puede convertir un string que no representa un número a un entero, esto genera un error

#Conversion a decimal
print(float("17.7")) #Convertir un string a un número decimal
print(float(7)) #Convertir un número entero a un número decimal

#Conversion a cadena de texto (String)
print(str(17)) #Convertir un número entero a una cadena de texto
print(str(7.9)) #Convertir un número decimal a una cadena de texto
print(str(True)) #Convertir un valor booleano a una cadena de texto

num = str(235) #str() convierte cualquier tipo de dato a una cadena de texto
print(str(num)) #Convertir un número entero a una cadena de texto
verdadero = str(True)
print(str(verdadero)) #Convertir un valor booleano a una cadena de texto

res = num + verdadero #Concatenar dos cadenas de texto
print(res) #Imprimir la concatenación de las dos cadenas de texto

#conversion a booleano (0, "", None, False) son considerados False, todo lo demás es True
print(bool(0)) #Convertir un número entero a un valor booleano
print(bool(123)) #Convertir un número entero a un valor booleano da true
print(bool("")) #Convertir una cadena vacía a un valor booleano da false
print(bool("hola")) #Convertir una cadena no vacía a un valor booleano da true

#Listas
tupla = (1, 2, 3) #Tupla
lista = list(tupla) #Convertir una tupla a una lista
print(lista) #Imprimir la lista

tupla2 = tuple(lista) #Convertir una lista a una tupla
print(tupla2) #Imprimir la tupla

#Conversion de diccionarios a claves o valores
diccionario = {"a": 1, "b": 2, "c": 3}
claves = list(diccionario.keys()) #Convertir las claves del diccionario a una lista
valores = list(diccionario.values()) #Convertir los valores del diccionario a una lista
print(claves) #Imprimir la lista de claves
print(valores) #Imprimir la lista de valores

#print(int("hola")) #Esto genera un error porque no se puede convertir un string que no representa un número a un entero
#print(list(123)) #Esto genera un error porque no se puede convertir un número entero a una lista

#Convierte una lista de booleanos en una lista de cadenas que representen True o Flase
