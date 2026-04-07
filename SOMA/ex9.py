prestacao = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa de juros (ex: 0.01 para 1%): "))
dias = int(input("Digite o tempo em dias: "))

nova_prestacao = prestacao + prestacao * taxa * dias
print("Nova prestação:", nova_prestacao)
