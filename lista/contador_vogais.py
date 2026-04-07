frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contagem = {v: frase.count(v) for v in vogais}
total = sum(contagem.values())
print("Total de vogais:", total)
print("Detalhes:", contagem)
