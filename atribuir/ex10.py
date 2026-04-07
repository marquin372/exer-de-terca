soma = 0
cont = 0
n = int(input("Digite o número de alunos: "))
for i in range(n):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    if 25 < idade < 40:
        soma += idade
        cont += 1
if cont > 0:
    media = soma / cont
    print("Média das idades entre 25 e 40:", media)
else:
    print("Nenhum aluno nessa faixa etária")
