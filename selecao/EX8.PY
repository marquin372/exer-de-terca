import math

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = b**2 - 4*a*c

if delta < 0 or a == 0:
    print("Não Existe Valores Reais")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes são:", x1, "e", x2)
