
def calcular_divida(divida):  #não esquece de colocar o propt pra adicionar o valor
    tabelaJuros = {
        1: 0,
        3: 0.10,
        6: 0.15,
        9: 0.20,
        12: 0.25
    }
    print("| Dívida     | Juros   | Parcelas  | Valor de cada parcela|")
    print("___________________________________________________________") #acho que essa tabela dá pro gasto...
    for parcelas, taxaJuros in tabelaJuros.items():
        Juros = divida * taxaJuros
        Total = divida + Juros
        Parcela = Total / parcelas
        print("_________________________________________________")
        print(f"| R$ {Total:.2f} | R$ {Juros:.2f} | {parcelas}         | R$ {Parcela:.2f} |")
        print("_________________________________________________")

valor_divida = float(input("Digite o valor da dívida: R$ "))

calcular_divida(valor_divida)
