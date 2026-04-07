N = int(input("Quantos números deseja digitar? "))
if N > 0:
    lista = []
    for i in range(N):
        lista.append(float(input(f"Número {i+1}: ")))
    print("Maior:", max(lista))
    print("Menor:", min(lista))
    print("Média:", sum(lista)/N)
else:
    print("N deve ser maior que 0.")
