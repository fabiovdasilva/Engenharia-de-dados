saldo = 2000
saque = 150


status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")