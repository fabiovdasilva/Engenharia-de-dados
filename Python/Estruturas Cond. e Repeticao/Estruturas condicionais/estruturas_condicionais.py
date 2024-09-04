saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque: 
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

opcao = int(input("Informe uma opcao:   [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo extrato...")
else:
    print("Opcao Invalida")

