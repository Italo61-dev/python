import os

restaurantes = []

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
    input('Pressione a tecla "ENTER" para voltar ao menu principal.')
    main()
     
def cadastra_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    #append == serve para empurrar os nome do restaurante para a lista
    restaurantes.append(nome_do_restaurante) 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Pressione a tecla "ENTER" para voltar ao menu principal.')
    main()

def listar_restaurantes():
    os.system('cls')
    print()

def escolher_opcao():
    opcao_escolha = int(input('Escolha uma opção: '))
    try:
        if opcao_escolha == 1:
            cadastra_novo_restaurante()
        elif opcao_escolha == 2: 
            listar_restaurantes()
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