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

