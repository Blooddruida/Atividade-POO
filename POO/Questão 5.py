def tabela_preco():
    preco_unit = 1.99
    print(f"{'Quantidade de Itens':<20}{'Valor Total (R$)':<20}")
    print("-" * 40)
    
    for quantidade in range(1, 51):
        valor = quantidade * preco_unit
        print(f"{quantidade:<20}{valor:<20.2f}")

def calcular_valor(itens):
    preco_unit = 1.99
    return itens * preco_unit

tabela_preco()

itens = int(input("Insira a quantidade de itens comprados pelo cliente: "))

valor = calcular_valor(itens)
print(f"O valor total para {itens} itens é: R$ {valor:.2f}")
