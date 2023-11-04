#   Faça uma carteira que converte moedas

real = float(input('Qual valor em real você quer converte para dolar, dolar canadense, euro? R$'))
dolar = real / 4.97
dolarCan = real / 3.60
euro = real / 5.26
print('\nO valor do dolar é 4.97, seu valor em dinheiro é {:.2f}, seu dinheiro covertido para dolar é de {:.2f}\n'.format(real, dolar))
print('O valor do dolar Canadense é 3.60, seu valor em dinheiro é {:.2f}, seu dinheiro covertido para dolar Canadense é de {:.2f}\n'.format(real, dolarCan))
print('O valor do euro é 5.26, seu valor em dinheiro é {:.2f}, seu dinheiro covertido para euro é de {:.2f}\n'.format(real, euro))