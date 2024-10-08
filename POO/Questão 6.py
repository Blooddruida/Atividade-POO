salario_inicial = 1000.00 #pq a valor sai bugado?
ano_inicial = 1995
ano_atual = 2025
aumento_percentual = 1.5 / 100
salario = salario_inicial

for ano in range(1996, ano_atual + 1):
    salario += salario * aumento_percentual
    
    aumento_percentual *= 2

print(f"Em {ano_atual} o Funcionario Recebera R$ {salario:.2f} como salario.")
