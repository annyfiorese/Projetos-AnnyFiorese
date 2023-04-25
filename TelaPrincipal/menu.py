import json
import os

def funcionalidades():
    print("Qual operação deseja realizar?")
    print("1 - Incluir")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Alterar")
    print("5 - Voltar")
    
    op = int(input())

    if 1 <= op <= 5:
        return op
    else:
        print("Opção inválida.")

def menu():
    print("\nOlá, seja bem-vindo ao nosso sistema acadêmico\n")
    print("Escolha uma opção:")
    print("1 - Alunos")
    print("2 - Professor")
    print("3 - Disciplinas")
    print("4 - Turma")
    print("5 - Matrícula")
    print("0 - Sair do programa")
    opcao = int(input())

    if 0 <= opcao <= 5:
        return opcao
    else:
        print("Opção inválida.")

def adicionar_dados(nome, nome_arquivo):

    if os.path.isfile(nome_arquivo):
        print("O arquivo já existe.")
    else:
        with open(nome_arquivo, "w") as arquivo_json:
            json.dump([], arquivo_json)
    # Carrega o conteúdo do arquivo JSON
    with open(nome_arquivo, 'r') as arquivo_json:
        lista = json.load(arquivo_json)

    # Verifica se o nome já está na lista
    if nome not in lista:
        # Adiciona o nome à lista
        lista.append(nome)

        # Grava a lista atualizada de nomes no arquivo JSON
        with open(nome_arquivo, 'w') as arquivo_json:
            json.dump(lista, arquivo_json)

        print("Nome adicionado com sucesso!")
    else:
        print("Nome já existe na lista.")
    
# Função para mostrar os nomes do arquivo JSON
def mostrar_nomes(arquivo):
    # Carrega o conteúdo do arquivo JSON
    with open(arquivo, 'r') as arquivo_json:
        lista = json.load(arquivo_json)

    print("Informações no arquivo JSON:")
    for nome in lista:
        print(nome)

# Função para excluir dados
def excluir_dados(info, nome_arquivo):
    # Abrir o arquivo JSON para leitura
    with open(nome_arquivo, "r") as arquivo_json:
        dados = json.load(arquivo_json)

    # Excluir um item da lista de dados
    item_a_excluir = info
    if item_a_excluir in dados:
        dados.remove(item_a_excluir)
        print("Item removido: ", item_a_excluir)
    else:
        print("Item não encontrado: ", item_a_excluir)

    # Escrever os dados atualizados de volta no arquivo JSON
    with open(nome_arquivo, "w") as arquivo_json:
        json.dump(dados, arquivo_json)

# Função para alterar dados 
def alterar_dados(nome_arquivo, nome_antigo, nome_novo):

    # Abrir o arquivo JSON para leitura
    with open(nome_arquivo, "r") as arquivo_json:
        dados = json.load(arquivo_json)
    # Verifica se o nome_antigo está na lista
    if nome_antigo in lista:
        # Encontra o índice do nome_antigo na lista
        index = lista.index(nome_antigo)
        # Substitui o nome_antigo pelo nome_novo
        lista[index] = nome_novo

        # Escrever os dados atualizados de volta no arquivo JSON
        with open(nome_arquivo, "w") as arquivo_json:
            json.dump(lista,arquivo_json)

        print("Nome alterado com sucesso!")
    else:
        print("Nome não encontrado na lista.")

# Função para voltar ao menu principal
def voltar_menu():
    input("Pressione ENTER para voltar ao menu principal...")

# Loop do programa
while True:
    opcao = menu()

    if opcao == 1:
        while True:
            op = funcionalidades()
            if op == 1:
                nome = input("Digite o nome do aluno: ")
                adicionar_dados(nome, "alunos.json")
            elif op == 2:
                mostrar_nomes("alunos.json")
            elif op == 3:
                nome = input("Digite o nome do aluno que deseja excluir: ")
                excluir_dados(nome, "alunos.json")
            elif op == 4:
                nome_antigo = input("Digite o nome do aluno que deseja alterar: ")
                nome_novo = input("Digite o novo nome do aluno: ")
                alterar_dados("alunos.json", nome_antigo, nome_novo)
            elif op == 5:
                break
            else:
                print("Opção inválida.")
        voltar_menu()
    elif opcao == 2:
        while True:
            op = funcionalidades()
            if op == 1:
                nome = input("Digite o nome do professor: ")
                cpf = int(input("Digite o CPF do professor: "))
                lista_professor = [nome,cpf]
                adicionar_dados(lista_professor, "professor.json")
            elif op == 2:
                mostrar_nomes("professor.json")
            elif op == 3:
                nome = input("Digite o nome do professor que deseja excluir: ")
                cpf = int(input("Digite o cpf do professor que deseja excluir: "))
                excluir = [nome,cpf]
                excluir_dados(excluir, "professor.json")
            elif op == 4:
                nome_antigo = input("Digite o nome do professor que deseja alterar: ")
                nome_novo = input("Digite o novo nome do professor: ")
                cpf_antigo = int(input("Digite o CPF do professor que deseja alterar: "))
                cpf_novo = int(input("Digite o novo CPF do professor: "))
                lista_dados_antigo = [nome_antigo,cpf_antigo]
                lista_dados_novo = [nome_novo,cpf_novo]
                alterar_dados("professor.json", lista_dados_antigo, lista_dados_novo)
            elif op == 5:
                break
            else:
                print("Opção inválida.")
        voltar_menu()
    elif opcao == 3:
        while True:
            op = funcionalidades()
            if op == 1:
                nome = input("Digite o nome do diciplina: ")
                codigo = int(input("Digite o codigo do diciplina: "))
                lista_diciplina = [nome,codigo]
                adicionar_dados(lista_diciplina, "diciplina.json")
            elif op == 2:
                mostrar_nomes("diciplina.json")
            elif op == 3:
                nome = input("Digite o nome do diciplina que deseja excluir: ")
                codigo = int(input("Digite o codigo do diciplina que deseja excluir: "))
                excluir = [nome,codigo]
                excluir_dados(excluir, "diciplina.json")
            elif op == 4:
                nome_antigo = input("Digite o nome do diciplina que deseja alterar: ")
                nome_novo = input("Digite o novo nome do diciplina: ")
                cod_antigo = int(input("Digite o codigo do diciplina que deseja alterar: "))
                cod_novo = int(input("Digite o novo codigo do diciplina: "))
                lista_dados_antigo = [nome_antigo,cod_antigo]
                lista_dados_novo = [nome_novo,cod_novo]
                alterar_dados("diciplina.json", lista_dados_antigo, lista_dados_novo)
            elif op == 5:
                break
            else:
                print("Opção inválida.")
        voltar_menu()
    elif opcao == 4:
        while True:
            op = funcionalidades()
            if op == 1:
                nome = input("Digite o nome da turma: ")
                codigo = int(input("Digite o codigo da turma: "))
                lista_turma = [nome,codigo]
                adicionar_dados(lista_turma, "turma.json")
            elif op == 2:
                mostrar_nomes("turma.json")
            elif op == 3:
                nome = input("Digite o nome da turma que deseja excluir: ")
                codigo = int(input("Digite o codigo da turma que deseja excluir: "))
                excluir = [nome,codigo]
                excluir_dados(excluir, "turma.json")
            elif op == 4:
                nome_antigo = input("Digite o nome da turma que deseja alterar: ")
                nome_novo = input("Digite o novo nome da turma: ")
                cod_antigo = int(input("Digite o codigo da turma que deseja alterar: "))
                cod_novo = int(input("Digite o novo codigo da turma: "))
                lista_dados_antigo = [nome_antigo,cod_antigo]
                lista_dados_novo = [nome_novo,cod_novo]
                alterar_dados("turma.json", lista_dados_antigo, lista_dados_novo)
            elif op == 5:
                break
            else:
                print("Opção inválida.")
        voltar_menu()
    elif opcao == 5:
        while True:
            op = funcionalidades()
            if op == 1:
                nome = input("Digite o nome do aluno: ")
                cpf = int(input("Digite o cpf do aluno: "))
                matricula = int(input("Digite o codigo do matricula: "))
                lista_matrucula = [nome,cpf,matricula]
                adicionar_dados(lista_matrucula, "matricula.json")
            elif op == 2:
                mostrar_nomes("matricula.json")
            elif op == 3:
                nome = input("Digite o nome do aluno que deseja excluir: ")
                cpf = int(input("Digite o nome do aluno que deseja excluir: "))
                codigo = int(input("Digite o codigo da matricula que deseja excluir: "))
                excluir = [nome,cpf,codigo]
                excluir_dados(excluir, "matricula.json")
            elif op == 4:
                nome_antigo = input("Digite o nome do aluno que deseja alterar: ")
                nome_novo = input("Digite o novo nome do aluno: ")
                cpf_antigo = int(input("Digite o cpf do aluno que deseja alterar: "))
                cpf_novo = int(input("Digite o novo cpf do aluno: "))
                cod_antigo = int(input("Digite o codigo de matricula que deseja alterar: "))
                cod_novo = int(input("Digite o nova matricula do aluno: "))
                lista_dados_antigo = [nome_antigo,cpf_antigo,cod_antigo]
                lista_dados_novo = [nome_novo,cpf_novo,cod_novo]
                alterar_dados("matricula.json", lista_dados_antigo, lista_dados_novo)
            elif op == 5:
                break
            else:
                print("Opção inválida.")
        voltar_menu()
    elif opcao == 0:
        print("Obrigado por utilizar o sistema acadêmico. Até mais!")
        break
    else:
        print("Opção inválida.")

