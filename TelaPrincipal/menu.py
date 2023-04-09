lista_estudante = []
print("Olá sejá bem vindo ao nosso sistema academico\n\n")
print("1 - Cadastro de Estudante\n")
print("2 - Professor\n")
print("3 - Diciplinas\n")
print("4 - Turma\n")
print("5 - Matricula\n")
print("6 - Menu de operações\n")
opcao = int(input(print("Escolha uma opção")))
if opcao == 1:
    alunos = True
    while alunos :
        aluno = input(print("Nome do Estudante: "))
        print("\n")
        print("\n")
        lista_estudante.append(aluno)
        print("1 - Novo aluno\n")
        opcao = int(input(print("2 - Listar Estudantes\n ")))
        if opcao == 2:
            alunos = False 
            for listar_estudante in lista_estudante:
                print(listar_estudante)
if opcao == 2:
    print("EM DESENVOLVIMENTO")    

if opcao == 3:
    print("EM DESENVOLVIMENTO")        

if opcao == 4:
    print("EM DESENVOLVIMENTO")

if opcao == 5:
    print("EM DESENVOLVIMENTO")

if opcao == 6:
    print("1 - Atualizar\n")
    print("2 - Excluir\n")
    op = input() 
    print("EM DESENVOLVIMENTO")