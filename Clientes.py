import os  # Importa o módulo 'os' para interagir com o sistema de arquivos (ex: verificar se um arquivo existe)
from colorama import (
    Fore,
    Style,
    init,
)  # Importa utilitários do colorama para cores e estilos no terminal

init(
    autoreset=True
)  # Inicializa o colorama e garante que as cores voltem ao padrão automaticamente após cada print


# Define a classe Cliente para encapsular os dados do cliente
class Cliente:

    # Método construtor da classe
    def __init__(self, nome, email, telefone):
        self.nome = nome  # Define o atributo nome
        self.email = email  # Define o atributo e-mail
        self.telefone = telefone  # Define o atributo telefone

    # Método para formatar os dados do cliente para gravação em arquivo (separados por ponto e vírgula)
    def f_arq(self):
        return f"{self.nome};{self.email};{self.telefone}\n"


# Função auxiliar para ler e estruturar os clientes a partir do arquivo
def ler_arquivo_clientes(arquivo):
    linhas = arquivo.readlines()  # Lê todas as linhas do arquivo e retorna uma lista de strings
    clientes_dado = []  # Lista para armazenar as tuplas com os dados dos clientes
    for linha in linhas:  # Percorre cada linha do arquivo
        dado = linha.strip().split(
            ";"
        )  # Remove espaços/quebras de linha e divide a string pelo caractere ';'

        if len(dado) == 3:  # Verifica se a linha possui exatamente 3 campos (nome, email, telefone)
            nome = dado[0]  # Obtém o nome
            email = dado[1]  # Obtém o e-mail
            telefone = dado[2]  # Obtém o telefone
            clientes_dado.append(
                (nome, email, telefone)
            )  # Adiciona a tupla formatada à lista de clientes

    return clientes_dado  # Retorna a lista contendo todos os clientes lidos


# Função de cadastro de um novo cliente
def cad_cliente():
    print(Style.BRIGHT + Fore.CYAN + "=" * 40)  # Exibe linha decorativa azul brilhante
    print(Style.BRIGHT + Fore.CYAN + "           Cadastro de Cliente")  # Exibe o título do menu
    print(Style.BRIGHT + Fore.CYAN + "=" * 40 + "\n")  # Exibe linha decorativa azul brilhante

    if os.path.exists("clientes.txt"):  # Verifica se o arquivo de clientes já existe no disco
        with open("clientes.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo para leitura
            clientes_dado = ler_arquivo_clientes(arquivo)  # Lê a lista de clientes existentes
            emails_cad = [
                c[1].lower() for c in clientes_dado
            ]  # Cria uma lista apenas com os e-mails em minúsculo
    else:
        emails_cad = []  # Se o arquivo não existir, inicia a lista de e-mails cadastrados como vazia

    while True:  # Loop de validação para a entrada do nome
        nome = input("Digite o nome do cliente: ").strip()  # Solicita o nome e remove espaços extras
        if not nome or not nome.replace(" ", "").isalpha():  # Valida se o nome contém apenas letras e não está vazio
            print(Fore.RED + "\nDigite um nome valido\n")  # Exibe mensagem de erro em vermelho
            continue  # Reinicia a leitura do nome
        break  # Sai do loop se a validação passar

    while True:  # Loop de validação para a entrada do e-mail
        email = input("\nDigite o e-mail: ").strip().lower()  # Solicita o e-mail e converte para minúsculas
        if not email or "@" not in email or "." not in email:  # Valida o formato básico do e-mail (presença de @ e .)
            print(Fore.RED + "\nDigite um e-mail valido!")  # Exibe mensagem de erro se inválido
            continue  # Reinicia o loop do e-mail

        if email in emails_cad:  # Verifica se o e-mail informado já está cadastrado no sistema
            print(Fore.RED + "\nCliente ja cadastrado com este e-mail!\n")  # Informa duplicidade em vermelho
            continue  # Reinicia o loop do e-mail
        break  # Sai do loop se o e-mail for válido e inédito

    while True:  # Loop de validação para a entrada do telefone
        telefone = input("\nDigite o telefone (somente numeros): ").strip()  # Solicita o telefone
        if not telefone.isdigit() or len(telefone) < 8:  # Verifica se contém apenas números e no mínimo 8 dígitos
            print(Fore.RED + "\nDigite um telefone valido!")  # Exibe erro em vermelho
            continue  # Reinicia o loop do telefone
        break  # Sai do loop se o telefone for válido

    novo_cliente = Cliente(nome, email, telefone)  # Instancia o objeto Cliente com os dados inseridos
    cad = novo_cliente.f_arq()  # Obtém a string formatada do cliente para arquivo
    with open("clientes.txt", "a", encoding="utf-8") as arquivo:  # Abre o arquivo em modo append ('a') para adicionar
        arquivo.write(cad)  # Escreve a linha do novo cliente no arquivo
        print(Style.BRIGHT + Fore.GREEN + "\nCliente cadastrado com sucesso!\n")  # Exibe mensagem de sucesso


# Função para listar todos os clientes cadastrados
def list_cliente():
    if not os.path.exists("clientes.txt"):  # Verifica se o arquivo existe
        print(Fore.RED + "\nArquivo nao encontrado\n")  # Exibe erro caso o arquivo ainda não tenha sido criado
        return  # Encerra a execução da função

    with open("clientes.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo para leitura
        clientes_dado = ler_arquivo_clientes(arquivo)  # Processa e lê os clientes salvos
        if not clientes_dado:  # Verifica se a lista retornada está vazia
            print(Fore.RED + "\nNenhum cliente encontrado\n")  # Exibe mensagem de alerta
            return  # Encerra a função

        print(Style.BRIGHT + Fore.CYAN + "=" * 55)  # Cabeçalho da listagem
        print(Style.BRIGHT + Fore.CYAN + "           Lista de Clientes")  # Título da listagem
        print(Style.BRIGHT + Fore.CYAN + "=" * 55 + "\n")  # Linha decorativa

        print(f"{'NOME': <20} {'E-MAIL': <22} {'TELEFONE': <12}")  # Exibe o cabeçalho das colunas com alinhamento à esquerda
        print("-" * 55)  # Divisor de colunas

        for nome, email, telefone in clientes_dado:  # Itera sobre cada cliente da lista
            print(f"{nome: <20} {email: <22} {telefone: <12}")  # Imprime os dados formatados em colunas
        print()  # Imprime uma linha em branco


# Função para alterar os dados de um cliente existente
def alt_cliente():
    if not os.path.exists("clientes.txt"):  # Verifica a existência do arquivo
        print(Fore.RED + "\nArquivo nao encontrado\n")  # Exibe erro em vermelho se não existir
        return  # Encerra a função

    with open("clientes.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo em modo leitura
        print(Style.BRIGHT + Fore.CYAN + "=" * 40)  # Exibe o cabeçalho decorativo
        print(Style.BRIGHT + Fore.CYAN + "           Alterar Cliente")  # Exibe o título
        print(Style.BRIGHT + Fore.CYAN + "=" * 40 + "\n")  # Linha decorativa
        clientes_dado = ler_arquivo_clientes(arquivo)  # Carrega os clientes existentes

    if not clientes_dado:  # Garante que existem registros a serem alterados
        print(Fore.RED + "Nenhum cliente encontrado\n")  # Alerta caso a lista esteja vazia
        return  # Encerra a função

    emails_cad = [c[1].lower() for c in clientes_dado]  # Cria lista de e-mails para verificação/busca

    while True:  # Loop de busca do cliente pelo e-mail
        email_busca = input("Digite o e-mail do cliente que deseja alterar: ").strip().lower()  # Solicita e-mail de busca

        if email_busca not in emails_cad:  # Verifica se o e-mail existe nos cadastros
            print(Fore.RED + "\nCliente nao encontrado. Tente novamente\n")  # Exibe erro caso não encontre
            return  # Retorna ao menu principal
        break  # Sai do loop se o e-mail for localizado

    indice = emails_cad.index(email_busca)  # Encontra a posição do cliente na lista original

    while True:  # Loop de validação do novo nome
        nov_nome = input("Digite o novo nome: ").strip()  # Lê o novo nome
        if not nov_nome or not nov_nome.replace(" ", "").isalpha():  # Valida se contém apenas letras
            print(Fore.RED + "\nDigite um nome valido\n")  # Exibe aviso de erro
            continue  # Repete a solicitação
        break  # Nome válido aceito

    while True:  # Loop de validação do novo e-mail
        nov_email = input("Digite o novo e-mail: ").strip().lower()  # Lê o novo e-mail
        if not nov_email or "@" not in nov_email or "." not in nov_email:  # Valida estrutura do e-mail
            print(Fore.RED + "\nDigite um e-mail valido")  # Exibe aviso de erro
            continue  # Repete a solicitação

        # Impede a duplicação de e-mail com outro usuário já cadastrado
        if nov_email in emails_cad and nov_email != email_busca:
            print(Fore.RED + "\nJa existe outro cliente cadastrado com esse e-mail\n")  # Informa duplicidade
            continue  # Repete a solicitação
        break  # Novo e-mail válido aceito

    while True:  # Loop de validação do novo telefone
        nov_tel = input("Digite o novo telefone: ").strip()  # Lê o novo telefone
        if not nov_tel.isdigit() or len(nov_tel) < 8:  # Valida se contém apenas números com tamanho correto
            print(Fore.RED + "\nDigite um telefone valido")  # Exibe aviso de erro
            continue  # Repete a solicitação
        break  # Novo telefone válido aceito

    clientes_dado[indice] = (nov_nome, nov_email, nov_tel)  # Atualiza os dados na tupla dentro da lista de registros

    with open("clientes.txt", "w", encoding="utf-8") as arquivo:  # Reabre o arquivo no modo sobrescrever ('w')
        for item_nome, item_email, item_tel in clientes_dado:  # Percorre toda a lista atualizada
            obj_cliente = Cliente(item_nome, item_email, item_tel)  # Instancia objeto temporário
            arquivo.write(obj_cliente.f_arq())  # Reescreve a nova lista no arquivo de texto

    print(Style.BRIGHT + Fore.GREEN + "\nCliente alterado com sucesso!\n")  # Exibe mensagem de confirmação


# Função para remover um cliente do arquivo
def rm_cliente():
    if not os.path.exists("clientes.txt"):  # Verifica se o arquivo existe
        print(Fore.RED + "\nArquivo nao encontrado\n")  # Exibe erro caso não exista
        return  # Encerra a função

    with open("clientes.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo para leitura
        print(Style.BRIGHT + Fore.CYAN + "=" * 40)  # Linha decorativa do menu
        print(Style.BRIGHT + Fore.CYAN + "           Remover Cliente")  # Título
        print(Style.BRIGHT + Fore.CYAN + "=" * 40 + "\n")  # Linha decorativa
        print(Fore.YELLOW + "Aviso: o cadastro do cliente sera removido")  # Mensagem de alerta amarela
        clientes_dado = ler_arquivo_clientes(arquivo)  # Carrega os clientes armazenados

    if not clientes_dado:  # Verifica se o arquivo contém clientes
        print(Fore.RED + "Nenhum cliente cadastrado\n")  # Informa que não há registros
        return  # Encerra a função

    email_rm = input("Digite o e-mail do cliente a ser removido: ").strip().lower()  # Solicita e-mail para remoção
    emails_cad = [c[1].lower() for c in clientes_dado]  # Cria lista com os e-mails cadastrados

    if email_rm not in emails_cad:  # Verifica se o e-mail inserido está presente no cadastro
        print(Fore.RED + "\nCliente nao encontrado\n")  # Informa se não existir
        return  # Retorna ao menu

    indice = emails_cad.index(email_rm)  # Descobre o índice da lista onde está o registro a remover

    with open("clientes.txt", "w", encoding="utf-8") as arquivo:  # Abre o arquivo para sobrescrever ('w')
        for i, item in enumerate(clientes_dado):  # Percorre os clientes mantendo a contagem do índice (i)
            if i != indice:  # Escreve de volta todos os clientes, MENOS o que bate com o índice que deve ser removido
                obj_cliente = Cliente(item[0], item[1], item[2])  # Cria o objeto cliente
                arquivo.write(obj_cliente.f_arq())  # Salva no arquivo

    print(Fore.GREEN + "\nCliente removido com sucesso!\n")  # Confirmação em verde


# Loop principal que mantém o programa rodando e exibe o menu
while True:
    print(Style.BRIGHT + Fore.CYAN + "=" * 40)  # Desenha a borda superior
    print(Style.BRIGHT + Fore.CYAN + "          Sistema de Clientes")  # Título do sistema
    print(Style.BRIGHT + Fore.CYAN + "=" * 40 + "\n")  # Desenha a borda inferior
    print("-" * 30)  # Separador de opções
    print(Fore.MAGENTA + "1- cadastrar cliente")  # Opção 1 em magenta
    print("-" * 30)  # Separador
    print(Fore.MAGENTA + "2- listar clientes")  # Opção 2 em magenta
    print("-" * 30)  # Separador
    print(Fore.MAGENTA + "3- alterar cliente")  # Opção 3 em magenta
    print("-" * 30)  # Separador
    print(Fore.MAGENTA + "4- remover cliente")  # Opção 4 em magenta
    print("-" * 30)  # Separador
    print("0- sair")  # Opção de saída em texto normal
    print("-" * 30)  # Separador

    try:  # Bloco try para capturar exceções se a entrada não for numérica
        opcao = int(input("\nescolha uma opcao: "))  # Solicita opção do usuário e converte para inteiro
        if opcao == 1:  # Se a opção escolhida for 1
            cad_cliente()  # Chama a função de cadastrar cliente
        elif opcao == 2:  # Se a opção escolhida for 2
            list_cliente()  # Chama a função de listar clientes
        elif opcao == 3:  # Se a opção escolhida for 3
            alt_cliente()  # Chama a função de alterar cliente
        elif opcao == 4:  # Se a opção escolhida for 4
            rm_cliente()  # Chama a função de remover cliente
        elif opcao == 0:  # Se a opção escolhida for 0
            print("\nFim do programa")  # Mensagem de encerramento
            break  # Interrompe o loop principal finalizando o programa
        else:
            print(Fore.RED + "\nPor favor, selecione uma opcao valida\n")  # Trata inteiros fora da faixa (ex: 5, 99)
    except ValueError:  # Trata exceções caso o usuário digite texto (não inteiro) no input
        print(Fore.RED + "\nSelecione uma opcao valida\n")  # Exibe aviso de erro genérico em vermelho