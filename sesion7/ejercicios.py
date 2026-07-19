#Ejercicio 1: Recibe la edad del usuario como cadena y la convierte a entero y calcula cuntos anios le faltan para llegar a 100
edad = input("Ingrese su edad: ") #La entrada de datos es una cadena (string)
edad_int = int(edad) #Convertir la cadena a un número entero
a_para100 = 100 - edad_int
print("Su edad es:", edad_int) #Imprimir la edad como un número entero
print(f"Te faltan {a_para100} años para cumplir a 100 años")


#Ejercicio2: Recibe una lista de números como cadena y la convierte a una lista de enteros y calcula la suma de los números
numeros_str = input("Ingrese una lista de números separados por comas: ") #La entrada de datos es una cadena (string)
numeros_lista_str = numeros_str.split(",") #Convertir la cadena a una lista de cadenas (string)
numeros_lista_int = [int(num) for num in numeros_lista_str] #Convertir la lista de cadenas a una lista de enteros, mediante una comprensión de listas, donde el ciclo for toma cada numero tomandolo de la lista inicial
suma = sum(numeros_lista_int) #Calcular la suma de los números en la lista
print("La suma de los números es:", suma) #Imprimir la suma de los números


#Convierte una lista de booleanos en una lista real de valores booleanos
num_bool = input("Ingrese una lista de booleanos separados por comas (True/False): ") #Introducir desde teclado los valores booleanos
num_bool_lista = [item.strip().lower() for item in num_bool.split(",")] #Toma la lista y la separa por las comas
bool_lista = [item == "true" for item in num_bool_lista]
print("La lista de booleanos es:", bool_lista)