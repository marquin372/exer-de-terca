soma = 0
for i in range(50):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    soma += idade
media = soma / 50
print("Média das idades:", media)
