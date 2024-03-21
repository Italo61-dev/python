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

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite qualquer tecla para voltar ao menu principal.')
    main()
    

def escolher_opcao():
    opcao_escolha = int(input('Escolha uma opção: '))
    try:
        if opcao_escolha == 1:
            print('Cadastrar restaurante')
        elif opcao_escolha == 2: 
            print('listar restaurantes')
        elif opcao_escolha == 3: 
            print('Ativar restaurante')
        elif opcao_escolha == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_progama()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()