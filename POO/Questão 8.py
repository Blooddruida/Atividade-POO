def verificar_nota():
    gabarito = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'e',7:'d',8:'c',9:'b',10:'a'}
    alunos = 0
    acertos = []
    while True:
        acertos_aluno = 0
        print("Responda as questões da prova (A, B, C, D, E):")
        for i in range(1, 11):
            resposta = input(f"Questão {i}: ").strip().upper()
            if resposta == gabarito[i]:
                acertos_aluno += 1
        acertos.append(acertos_aluno)
        alunos += 1
        continuar = input("Outro aluno vai utilizar o sistema?: ").strip().lower()
        if continuar != 'sim':
            break
    maior_acerto = max(acertos)
    menor_acerto = min(acertos)
    media_notas = sum(acertos) / alunos if alunos > 0 else 0
    print(f"Total de Alunos: {alunos}")
    print(f"Maior Acerto: {maior_acerto}")
    print(f"Menor Acerto: {menor_acerto}")
    print(f"Média das Notas: {media_notas:.2f}")
verificar_nota()
