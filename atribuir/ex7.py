soma = 0
n = int(input("Digite o número de alunos: "))
for i in range(n):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    if nota >= 5.0:
        soma += nota
print("Soma das notas ≥ 5.0:", soma)
