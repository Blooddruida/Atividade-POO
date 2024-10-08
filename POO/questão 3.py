def nprimo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
numero = int(input("Digite um número inteiro: "))
if nprimo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
