raio = float(input("Digite o raio: "))
altura = float(input("Digite a altura: "))
pi = 3.14

area_base = pi * raio**2
area_lateral = 2 * pi * raio * altura
area_total = 2 * area_base + area_lateral
print("Área do cilindro:", area_total)
