Pares = 0 #acho que tá faltando alguma coisa em uma parte
Impares = 0
for i in range(10):
    num = int(input(f"Digite o número inteiro:"))
    if num % 2 == 0:
        Pares += 1
    else:
        Impares += 1


print(f"Quantidade de números pares: {Pares}")
print(f"Quantidade de números ímpares: {Impares}")
