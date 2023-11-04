#   Faça um progama que leia o seu valor, seu antecessor e seu sucessor

value = int(input('Digite um número, para mostra seu antecessor e seu sucessor: '))
before = value - 1
after = value + 1
print(f'Analisando seu valor {value}, seu antecessor é {before} e seu sucessor é {after}.')