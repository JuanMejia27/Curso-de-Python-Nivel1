texto = "hola, mundo"
letra = texto[0] #toma la letra en la posicion que se refiera, en este caso la letra h
print(texto)
print(letra)

'''texto_simple = 'hola, mundo'
texto_triple = """hola, mundo
ls respuesdta es: 42,
en el cual puedes ver que se puede escribir en varias lineas"""'''

#concatenacion de cadenas
saludo = "hola" + " , " + "mundo"
print(saludo)

#repeticion de cadenas
repeticion = "Python! " * 3 #toma la cadena y la repite n veces
print(repeticion)

#interpolacion de cadenas
x = 22
y = 10 #puede ser con uso de variables o directamente con numeros o letras/palabras
a = x + y
resultado = f"la suma es: {a}" #se puede usar f para interpolar variables dentro de la cadena
print(resultado)

#slicing (subcadena), que se refiere a tomar un pedazo de la cadena, en este caso desde la posicion 0 hasta la 4
cadena = "hola, Python!"
subcadena = cadena[6:13] #toma desde la posicion 7 hasta la 13
print(subcadena)

#Metodos Upper y Lower
print ("hola".upper()) #convierte a mayusculas
print ("MUNDO".lower()) #convierte a minusculas

#Metodos Strip, Lstrip y Rstrip
text = "   hola, A todos   "
print(text.strip())  #elimina espacios en blanco al principio y al final
print(text.lstrip())  #elimina espacios en blanco al principio
print(text.rstrip())  #elimina espacios en blanco al final

#Metodo Replace
nombre = "Python, como lenguaje de programacion"
frase = f"Me gusta {nombre}" #usando f para interpolar la variable nombre dentro de la cadena
print(frase.replace("Python", "Java")) #reemplaza una palabra por otra

#metodos split y join
lista = nombre.split()  #divide la cadena en una lista de strings
print(lista)
nueva_cadena = " ".join(lista)  #une la lista de strings en una sola cadena
print(nueva_cadena)

# Metodo find 
print("Hola mundo como estan".find("o")) #busca la palabra y devuelve la posicion de la primera letra de la palabra, si no encuentra devuelve -1

# metodos startswith y endswith
print("Python es genial".startswith("genial")) #devuelve True si la cadena empieza
print("Python es genial".endswith("genial")) #devuelve True si la cadena termina