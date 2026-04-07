num = int(input("Digite um número: "))
limite = int(input("Até qual número da tabuada? (ex: 10, 20): "))
for i in range(1, limite+1):
    print(f"{num} x {i} = {num*i}")
