import os
def exibir_nome_progama():
    print("""
    
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗░█████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░██║░░██║
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗██║░░██║
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝╚█████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░░╚════╝░
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante\n2. Listar restaurantes\n3. Ativar restaurante\n4. Sair')

def finalizar_app():
    os.system('cls')
    # os.system('clear')
    print('Finalizando o app\n')

def escolher_opcao():
    opcao_escolha = int(input('Escolha uma opção: '))



    if opcao_escolha == 1:
        print('Cadastrar restaurante')
    elif opcao_escolha == 2: 
        print('listar restaurantes')
    elif opcao_escolha == 3: 
        print('Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome_progama()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()