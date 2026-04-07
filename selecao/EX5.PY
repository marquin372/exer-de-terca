a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
    print("Triângulo Isósceles")
else:
    print("Não é Isósceles")
