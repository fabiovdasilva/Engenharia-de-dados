curso = "Python"

print(curso.center(10, "#"))

print(curso.upper())
print(curso.lower())
print(curso.title())

texto = " olá mundo!    "

print(texto)

print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")


menu = "HelloWorld"

print("####" + menu + "####")

print(menu.center(30) + ".")

print(menu.center(20, "#"))

for letra in menu:
    print(letra, end="-")

print("-".join(menu))