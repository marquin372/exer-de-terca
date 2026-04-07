soma = 0
n = int(input("Digite o número de alunos: "))
for i in range(n):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    if idade > 25:
        soma += idade
print("Soma das idades > 25:", soma)
