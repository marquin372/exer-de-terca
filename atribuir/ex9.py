cont = 0
n = int(input("Digite o número de alunos: "))
for i in range(n):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    if idade == 30:
        cont += 1
print("Quantidade de alunos com 30 anos:", cont)
