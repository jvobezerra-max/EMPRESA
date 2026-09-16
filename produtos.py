import os  # Importando o módulo OS
from colorama import Fore, Style, init  # Importando o módulo colorama

init()  # Inicializando o colorama


def Menu(): #Função Menu
    while True: #Definindo um loop pro menu
        print(Fore.CYAN + "\nSeja bem-vindo ao sistema de cadastro de produtos!")
        print(Fore.MAGENTA + "\nSISTEMA DE CADASTRO DE PRODUTOS")
        print(Fore.GREEN + "1 - Cadastrar produto")
        print(Fore.BLUE + "2 - Listar produtos")
        print(Fore.YELLOW + "3 - Alterar produto")
        print(Fore.RED + "4 - Excluir produto")
        print(Fore.BLACK + "0 - Sair")

        try:
            escolha = int(input("Escolha uma opção: ").strip()) #Escolha do usuário

            if 0 <= escolha <= 4: #Não deixa o usuário digitar numeros que não estão entre 0 e 4
                return escolha 
            else:
                print(Fore.RED + "Opção inválida!​") 

        except ValueError:
            print(Fore.RED + "Digite apenas números.") #Não deixa o usuário digitar letras ou caracteres especiais


def cadastrar_produto(): #Função cadastrar produto
    print(Fore.CYAN + "CADASTRO DE PRODUTO")
    print(Fore.MAGENTA + "Informe os dados do produto." + Style.RESET_ALL)

    while True:
        nome = input("Digite o nome do produto: ").strip() #Solicita o nome do produto e remove espaços no inicio e no fim

        if nome == "": #Não deixa ser um nome vazio
            print(Fore.RED + "Nome inválido. Preencha corretamente." + Style.RESET_ALL)
            continue #Continua o loop caso seja inválido

        invalido = False #Variável para verificar se o nome é inválido, ela começa como falsa até que se prove o contrário

        for char in nome:
            if char.isdigit() or (not char.isalnum() and char != " "): #Verifica se o nome contém caracteres inválidos
                invalido = True #Marca o nome como inválido
                break #Sai do loop caso encontre um caractere inválido

        if invalido:
            print(Fore.RED + "Nome inválido. Preencha corretamente." + Style.RESET_ALL)
            continue #Se for inválido, continua o loop até ser válido

        break #Sai do loop caso o nome seja válido

    while True:
        try:
            preco = input("Digite o preço do produto: ").strip() #Solicita o preço do produto e remove espaços no inicio e fim
            preco = preco.replace(",", ".") #Deixa que o usuário digite o preço com vírgula ou ponto
            preco = float(preco) #Converte o preço pra float

            if preco < 0: #Não deixa o usuário digitar preços negativos
                print(Fore.RED + "Preço inválido​. Preencha corretamente." + Style.RESET_ALL) #Se for inválido, continua o loop até ser válido
                continue #Continua o loop caso seja inválido

            break #Sai do loop caso o preço seja válido

        except ValueError: #Se o usuário digitar letras ou carcteres especiais, o programa vai mostrar mensagem de erro e continuar o loop
            print(Fore.RED + "Preço inválido​. Preencha corretamente." + Style.RESET_ALL)

    
    while True:
        try:
            quantidade = int(input("Digite a quantidade desejada: "))
            if quantidade < 0:
                print(Fore.RED + "Quantidade inválida. Preencha corretamente." + Style.RESET_ALL)
                continue
            break
        except ValueError:
            print(Fore.RED + "Quantidade inválida​. Preencha corretamente." + Style.RESET_ALL)

    print(Fore.GREEN + "Produto cadastrado com sucesso!​") #Sucesso ao cadastrar produto

    with open("produtos.txt", "a", encoding="utf-8") as arquivo: #Abre o arquivo produtos.txt no modo de escrita, caso não exista, ele cria um novo arquivo. encoding="utf-8" é usado pra evitar problemas com acentuação
            arquivo.write(f"{nome}|{preco}|{quantidade}\n") #Escreve o nome e o preço do produto no arquivo, separados por vírgula e adiciona uma nova linha no final


def listar_produtos(): #Função listar produtos
    print(Fore.MAGENTA + "LISTA DE PRODUTOS") 

    if not os.path.exists("produtos.txt"): #Verifica se o arquivo txt existe, caso não exista, ele mostra erro
        print(Fore.RED + "Nenhum aluno cadastrado." + Style.RESET_ALL)
        return

    with open("produtos.txt", "r", encoding="utf-8") as arquivo: #Abre o arquivo produtos.txt no modo leitura - read
        produtos = arquivo.readlines() #Lê todas as linhas do arquivo e armazena na variável produtos

    if not produtos: #Se não houver alunos cadastrados, ele mostra erro
        print(Fore.RED + "Nenhum aluno cadastrado." + Style.RESET_ALL)
        return

    for produto in produtos: #Para cada produto em produtos
        nome, preco, quantidade = produto.strip().split("|") #Separa o nome, preço e quantidade do produto
        preco = float(preco) #Converte o preço para número decimal
        quantidade = int(quantidade) #Converte a quantidade para número inteiro


        print(f"\n{Fore.CYAN}Produto: {nome} --------~ {Style.RESET_ALL}{Fore.GREEN}Preço: {preco:.2f} --------~ {Style.RESET_ALL}{Fore.YELLOW}Quantidade: {quantidade}{Style.RESET_ALL}") #Mostra os dados do produto

def alterar_produto(): #Função alterar produto
    print(Fore.CYAN + "ALTERAR PRODUTO") 

    if not os.path.exists("produtos.txt"): #Se não houver o arquivo, mostra mensagem de erro
        print(Fore.RED + "Nenhum produto cadastrado." + Style.RESET_ALL)
        return

    with open("produtos.txt", "r", encoding="utf-8") as arquivo: #Abre o arquivo pra leitura
        produtos = arquivo.readlines() #Lê os produtos cadastrados e armazena em uma lista

    if not produtos: #Se não achar produtos, mostra nenhum produto cadastrado
        print(Fore.RED + "Nenhum produto cadastrado." + Style.RESET_ALL)
        return

    print(Fore.YELLOW + "\nProdutos cadastrados:" + Style.RESET_ALL) #Mostra os produtos cadastrados

    for produto in produtos:
        nome, preco, quantidade = produto.strip().split("|") #Separa o nome, preço e quantidade do produto
        preco = float(preco) #Converte o preço para número decimal antes de formatar
        print(f"\n{Fore.CYAN}Produto: {nome} --------~ {Style.RESET_ALL}{Fore.GREEN}Preço: {preco:.2f} --------~ {Style.RESET_ALL}{Fore.YELLOW}Quantidade: {quantidade}{Style.RESET_ALL}") #Mostra os dados do produto 

    while True:
        alteracao = input("\nDigite o nome do produto que deseja alterar: ").strip() #Pede o nome pro usuário de quem deseja alterar

        if alteracao == "": #Se for vázio, dá erro
            print(Fore.RED + "Nome inválido.​" + Style.RESET_ALL)
            continue

        encontrado = False #Variável para encontrar, começa como falsa até que se mostre verdadeira

        for produto in produtos:
            nome, preco, quantidade = produto.strip().split("|")

            if nome.lower() == alteracao.lower(): #Compara o nome ignorando letras maiúsculas e minúsculas
                encontrado = True 
                break

        if encontrado: #Se encontrar, quebra o loop
            break

        print(Fore.RED + "Produto não encontrado." + Style.RESET_ALL)

    while True:
        nome = input("Digite o novo nome: ").strip() #Pede um novo nome 

        if nome == "": #Não deixa ser vázio
            print(Fore.RED + "Nome inválido.​" + Style.RESET_ALL)
            continue #Continua o loop

        invalido = False #Variável que verifica se o novo nome possui caracteres inválidos

        for char in nome:
            if char.isdigit() or (not char.isalnum() and char != " "): #Verifica se o novo nome contém caracteres inválidos
                invalido = True
                break

        if invalido:
            print(Fore.RED + "Nome inválido.​" + Style.RESET_ALL)
            continue

        break

    while True:
        try:
            novo_preco = input("Digite o novo preço: ").strip() #Solicita o novo preço do produto
            novo_preco = float(novo_preco.replace(",", ".")) #Converte o novo preço para float e deixa usarem vírgula

            if novo_preco < 0: #Não deixa o usuário digitar preços negativos
                print(Fore.RED + "Preço inválido.​" + Style.RESET_ALL)
                continue

            break

        except ValueError: #Impede que o programa pare caso o usuário digite um valor inválido
            print(Fore.RED + "Preço inválido.​" + Style.RESET_ALL)
    while True:
        try:
            nova_quantidade = int(input("Digite a nova quantidade: ")) #Solicita a nova quantidade
            if nova_quantidade < 0: #Não deixa o usuário digitar quantidade negativa
                print(Fore.RED + "Quantidade inválida.​" + Style.RESET_ALL)
                continue
            break
        except ValueError:
            print(Fore.RED + "Quantidade inválida.​" + Style.RESET_ALL)

    for i in range(len(produtos)): #Percorre a lista de produtos para encontrar o produto que será alterado
        nome_antigo, preco, quantidade = produtos[i].strip().split("|")

        if nome_antigo.lower() == alteracao.lower(): #Verifica se encontrou o produto escolhido
            produtos[i] = f"{nome}|{novo_preco}|{nova_quantidade}\n" #Substitui os dados antigos pelos novos, mantendo o separador "|"
            break

    with open("produtos.txt", "w", encoding="utf-8") as arquivo: #Abre o arquivo para reescrever os dados atualizados
        for produto in produtos:
            arquivo.write(produto)

    print(Fore.GREEN + "Produto alterado com sucesso! ✅​" + Style.RESET_ALL)


def excluir_produto(): #Função para excluir produto
    print(Fore.CYAN + "EXCLUIR PRODUTO")

    if not os.path.exists("produtos.txt"): #Verifica se o arquivo existe
        print(Fore.RED + "Nenhum produto cadastrado." + Style.RESET_ALL)
        return

    with open("produtos.txt", "r", encoding="utf-8") as arquivo: #Abre o arquivo para leitura
        produtos = arquivo.readlines() #Lê os produtos cadastrados

    if not produtos: #Verifica se existem produtos cadastrados
        print(Fore.RED + "Nenhum produto cadastrado." + Style.RESET_ALL)
        return

    print(Fore.YELLOW + "\nProdutos cadastrados:")

    for produto in produtos:
        nome, preco, quantidade = produto.strip().split("|") #Separa o nome, preço e quantidade do produto
        preco = float(preco)
        print(f"\n{Fore.CYAN}Produto: {nome} --------~ {Style.RESET_ALL}{Fore.GREEN}Preço: {preco:.2f} --------~ {Style.RESET_ALL}{Fore.YELLOW}Quantidade: {quantidade}{Style.RESET_ALL}") #Mostra os dados do produto
    excluir = input(Fore.MAGENTA +"\nDigite o nome do produto que deseja excluir: ").strip() #Pede o nome do produto que será excluído

    if excluir == "": #Não deixa o nome ser vazio
        print(Fore.RED + "Nome inválido.❌​" + Style.RESET_ALL)
        return

    nova_lista = [] #Cria uma lista para armazenar os produtos que não serão excluídos
    encontrado = False #Verifica se o produto foi encontrado

    for produto in produtos:
        nome, preco, quantidade = produto.strip().split("|")

        if nome.lower() == excluir.lower(): #Verifica se o nome corresponde ao produto escolhido
            encontrado = True
        else:
            nova_lista.append(produto) #Mantém na lista os produtos que não serão excluídos

    if encontrado:
        with open("produtos.txt", "w", encoding="utf-8") as arquivo: #Reescreve o arquivo sem o produto excluído
            for produto in nova_lista:
                arquivo.write(produto)

        print(Fore.GREEN + "Produto excluído com sucesso!✅​" + Style.RESET_ALL)

    else:
        print(Fore.RED + "Produto não encontrado." + Style.RESET_ALL)


def sair(): #Função para encerrar o sistema
    print(Fore.MAGENTA + "Saindo do sistema...")


while True: #Mantém o sistema funcionando até o usuário escolher sair
    opcao = Menu() #Chama o menu e armazena a opção escolhida

    if opcao == 1: #Executa o cadastro de produto
        cadastrar_produto()

    elif opcao == 2: #Executa a listagem de produtos
        listar_produtos()

    elif opcao == 3: #Executa a alteração de produto
        alterar_produto()

    elif opcao == 4: #Executa a exclusão de produto
        excluir_produto()

    elif opcao == 0: #Encerra o programa
        sair()
        break #Interrompe o loop principal