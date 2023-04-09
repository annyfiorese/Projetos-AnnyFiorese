lista_estudante = []

while True:
    print("\nOlá, seja bem-vindo ao nosso sistema acadêmico\n")
    print("Escolha uma opção:")
    print("1 - Cadastro de Estudante")
    print("2 - Professor")
    print("3 - Disciplinas")
    print("4 - Turma")
    print("5 - Matrícula")
    print("6 - Menu de operações")
    print("0 - Sair do programa")

    opcao = int(input())

    if opcao == 1:
        while True:
            aluno = input("Nome do Estudante: ")
            lista_estudante.append(aluno)
            print("1 - Novo aluno")
            print("2 - Listar Estudantes")
            print("0 - Voltar ao menu principal")
            opcao = int(input())
            if opcao == 0:
                break
                
        for listar_estudante in lista_estudante:
            print(listar_estudante)

    elif opcao == 2:
        print("EM DESENVOLVIMENTO")
        
    elif opcao == 3:
        print("EM DESENVOLVIMENTO")
        
    elif opcao == 4:
        print("EM DESENVOLVIMENTO")
        
    elif opcao == 5:
        print("EM DESENVOLVIMENTO")
        
    elif opcao == 6:
        while True:
            print("Escolha uma opção:")
            print("1 - Atualizar")
            print("2 - Excluir")
            print("0 - Voltar ao menu principal")
            op = input() 
            if op == "0":
                break
            print("EM DESENVOLVIMENTO")
        
    elif opcao == 0:
        print("Saindo do programa...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")
