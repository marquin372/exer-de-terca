soma = 0
cont = 0
n = int(input("Digite o número de alunos: "))
for i in range(n):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    if 5.0 < nota < 7.0:
        soma += nota
        cont += 1
if cont > 0:
    media = soma / cont
    print("Média das notas entre 5.0 e 7.0:", media)
else:
    print("Nenhum aluno nessa faixa de notas")
