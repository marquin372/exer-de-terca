a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

# Considerando c como a hipotenusa
if abs(c**2 - (a**2 + b**2)) < 1e-9:  # tolerância para números reais
    print("Triângulo Retângulo")
else:
    print("Não é Retângulo")
