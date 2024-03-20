# Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

insira_numero = int(input('Insira um número: '))

if insira_numero % 2 == 0:
    print(insira_numero, 'Esse número é par')
else:
    print(insira_numero, 'Esse número é impar')

# Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

insira_idade = int(input('Insira sua idade: '))

if insira_idade <= 12:
    print('Criança')
elif insira_idade <= 18:
    print('Adolescente')
else:
    print('Alduto')

# Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
    
usuario_esperado = 'Italo'
senha_esperada = 'Italo123'

usuario = input('Insira o nome do usuário: ')
senha = input('insira a senha: ')

if usuario == usuario_esperado and senha == senha_esperada:
    print('Usuário cadastrado')
else:
    print('usuário não cadastrado')