cont = 0
for i in range(100):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    if idade == 30:
        cont += 1
print("Quantidade de alunos com 30 anos:", cont)
