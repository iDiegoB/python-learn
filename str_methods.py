# se pueden definir en variables, no es necesario usar el print
name = "Diego Barra"
#upper hace mayusculas
print(name.upper())

#lower hace minusculas
print(name.lower()) 

#title hace la primera letra de cada palabra mayuscula
print(name.title())     

#capitalize hace la primera letra mayuscula
print(name.capitalize())    

#swapcase invierte mayusculas y minusculas
print(name.swapcase())  

#split divide un string en una lista
print(name.split()) # por defecto separa por espacios, pero se puede pasar un parametro ejemplo: name.split(",")

#join une una lista de strings en un solo string
print(", ".join(["Hola", "Mundo"])) # por defecto une con espacios

#se puede pasar un parametro ejemplo: "-".join(["Hola", "Mundo"])
print(" xd ".join(["Hola", "Mundo","Hola", "Mundo"]))

#replace reemplaza una subcadena por otra
print(name.replace("Diego", "Pepe"))

#startswith hace true si empieza con la subcadena  
print(name.startswith("Diego"))

#endswith hace true si termina con la subcadena
print(name.endswith("Barra"))

#find devuelve la posicion de la subcadena, -1 si no la encuentra
print(name.find("Barra"))

print(name.find("Pepe"))  # returns -1 if not found

#count cuenta cuantas veces aparece la subcadena
print(name.count("a"))

#len devuelve la longitud del string
print(len(name))

#isalpha devuelve true si todos los caracteres son letras
print(name.isalpha())  # False because of space

#isalnum devuelve true si todos los caracteres son letras o numeros
print(name.isalnum())  # False because of space

#isdigit devuelve true si todos los caracteres son numeros
print(name.isdigit())  # False

#isspace devuelve true si todos los caracteres son espacios
print(name.isspace())  # False

#strip elimina espacios al inicio y al final
print("   Hola   ".strip())

#lstrip elimina espacios al inicio
print("   Hola   ".lstrip())

#rstrip elimina espacios al final
print("   Hola   ".rstrip())

#center centra el string en un espacio de longitud dada, rellenando con el caracter dado
print("Hola".center(20, "*"))

#ljust alinea a la izquierda en un espacio de longitud dada, rellenando con el caracter dado
print("Hola".ljust(20, "*"))

#rjust alinea a la derecha en un espacio de longitud dada, rellenando con el
print("Hola".rjust(20, "*"))

#zfill rellena con ceros a la izquierda hasta la longitud dada
print("Hola".zfill(10))

#encode codifica el string en bytes
print("Hola".encode())

#format formatea el string
print("Hola".format())

#format con parametros para formatear
print("Hola, {}!".format(name))

#f-string hace lo mismo que format pero mas facil de leer
print(f"Hola, {name}!")
print("Hola, {nombre}!".format(nombre=name))
print("Hola, {0} {1}!".format("Diego", "Barra"))
print("Hola, {1} {0}!".format("Diego", "Barra"))
print("Hola, {nombre} {apellido}!".format(nombre="Diego", apellido="Barra"))

#format_map con diccionario hace lo mismo que format con parametros
print("Hola, {nombre} {apellido}!".format_map({"nombre": "Diego", "apellido": "Barra"}))
print("Hola, {} {}!".format("Diego", "Barra"))