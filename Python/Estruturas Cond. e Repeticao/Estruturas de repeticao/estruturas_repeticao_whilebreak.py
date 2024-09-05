# while True:
#     numero = int(input("Informe um número: "))

#     if numero == 10:
#         break

#     print(numero)


for numero in range(100):
    if numero == 10:
        break

    print(numero, end="  ")


for numero2 in range(100):
    if numero2 == 12:
        continue  #continue vai chegar na condicao, pular e continuar
        break
    print(numero2, end="  ")


    # Break parar a execucao
    # Continue pular a execucao
    