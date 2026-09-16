import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

while True:
    print(Fore.CYAN + Style.BRIGHT + "\n==============================")
    print(Fore.YELLOW + Style.BRIGHT + "  SISTEMA DE GERENCIAMENTO  ")
    print(Fore.CYAN + Style.BRIGHT + "==============================")
    print(Fore.GREEN + "1." + Fore.WHITE + " Gerenciar Clientes")
    print(Fore.GREEN + "2." + Fore.WHITE + " Gerenciar Produtos")
    print(Fore.RED + "0." + Fore.WHITE + " Sair do Sistema")
    print(Fore.CYAN + Style.BRIGHT + "==============================")
    
    opcao = input(Fore.BLUE + "Escolha uma opção: " + Style.RESET_ALL)

    if opcao == "1":
        subprocess.run(["python", "Clientes.py"])
    elif opcao == "2":
        subprocess.run(["python", "produtos.py"])
    elif opcao == "0":
        print(Fore.RED + "\nEncerrando o sistema...")
        break
    else:
        print(Fore.RED + "Opção inválida! Tente novamente.")
