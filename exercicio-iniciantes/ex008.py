#   Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valueProduct = float(input('Digite o valor do produto? '))  
discount = 0.05
newValue = valueProduct - (valueProduct * discount) 
print(f'O seu produto de R${valueProduct}, irá sair por R${newValue}, com o desconto de 5%.')