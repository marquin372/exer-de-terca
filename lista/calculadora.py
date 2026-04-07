def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else "Erro: divisão por zero"

print("Escolha a operação: 1-Somar, 2-Subtrair, 3-Multiplicar, 4-Dividir")
op = int(input("Opção: "))
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

if op == 1:
    print("Resultado:", somar(x, y))
elif op == 2:
    print("Resultado:", subtrair(x, y))
elif op == 3:
    print("Resultado:", multiplicar(x, y))
elif op == 4:
    print("Resultado:", dividir(x, y))
else:
    print("Opção inválida.")
