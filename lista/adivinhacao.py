import random
segredo = random.randint(1, 100)
tentativas = 0
acertou = False

while not acertou:
    chute = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1
    if chute == segredo:
        print("Parabéns! Você acertou em", tentativas, "tentativas.")
        acertou = True
    elif chute < segredo:
        print("O número é maior!")
    else:
        print("O número é menor!")
