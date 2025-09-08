text = "Diego Barra"
print(text[0:5:1])#muestra desde el indice 0 hasta el 5 (sin incluir el 5) de 1 en 1
print(text[6:])
print(text[:6])
print(text[::])
print(text[::-1]) #muestra el string al reves
print(text[-1:-6:-1]) #muestra los ultimos 5 caracteres al reves
print(text[-5:]) #muestra los ultimos 5 caracteres
print(text[:-6]) #muestra todo menos los ultimos 5 caracteres
print(text[::3]) #muestra de 3 en 3 caracteres

text = "Hola Mundo"
new_text = text[:5] + text[5:].replace("Mundo", "Python")
print(new_text)

text = "python es genial"
parts = text.split()
parts2 = parts[:2] + ["muy"] + parts[2:]
print(parts)
print(parts2)
parts_reverse = parts[::-1]
print(parts_reverse)
text_reversed = " ".join(parts_reverse)
print(text_reversed)

text = "Python"
print(text[:2].lower() + text[2:].upper())

text = '   hola python    '
print(text.strip().capitalize().title())
print(text.strip()[:5])
print(text.strip()[5:])
