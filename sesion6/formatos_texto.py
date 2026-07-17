texto_multilinea = '''Hola
como se encuentran todos?
Yo me encuentro bien''' #se puede usar triple comilla simple o doble para escribir en varias lineas

edad = 32
msj = "tengo  {} años".format(edad) #se ppuede usar el metodo format para interpolar variables dentro de la cadena
print(msj)

#Tarea: Crear una funcion que reciba un nombre completo y despues formatee de manera que todas las primeras letras de cada palabra esten en mayusculas.

def formatear_nombre(nombre):
    #return nombre.title() #el metodo title convierte la primera letra de cada palabra en mayuscula
    #return nombre.upper() #el metodo upper convierte todas las letras en mayusculas
    #return nombre.lower() #el metodo lower convierte todas las letras en minusculas
    return nombre.split() #el metodo split divide la cadena en una lista de palabras
    
#print(formatear_nombre("juan antonio perez garcia")) #ejemplo de uso de la funcion
print(formatear_nombre("Me gusta usar Python")) #ejemplo de uso de la funcion
    