soma = 0
n = int(input("Digite o número de alunos: "))
for i in range(n):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma += nota
media = soma / n
print("Média das notas:", media)
