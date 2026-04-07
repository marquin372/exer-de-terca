while True:
    print("\nMenu:")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        with open("tarefas.txt", "a") as arquivo:
            arquivo.write(tarefa + "\n")
        print("Tarefa adicionada!")
    elif opcao == "2":
        try:
            with open("tarefas.txt", "r") as arquivo:
                tarefas = arquivo.readlines()
            if tarefas:
                for i, t in enumerate(tarefas, 1):
                    print(f"{i}. {t.strip()}")
            else:
                print("Nenhuma tarefa encontrada.")
        except FileNotFoundError:
            print("Arquivo ainda não existe.")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
