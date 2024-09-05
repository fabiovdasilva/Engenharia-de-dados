#
texto = input ("Informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

#Else opcional for/else
else:  
    print()