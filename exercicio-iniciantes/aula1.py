#   Faça um progama que leia o seu valor, seu antecessor e seu sucessor

""" value = int(input('Digite um número, para mostra seu antecessor e seu sucessor: '))
before = value - 1
after = value + 1
print(f'Analisando seu valor {value}, seu antecessor é {before} e seu sucessor é {after}.') """
#-----------------------------------------------------------------------------

#   Faça um progama que leia seu drobro seu triplo e sua raiz quadrada

""" value = float(input('Digite um valor: '))
double = value * 2
triple = value * 3
squareRoot = value ** 0.5
print('Seu valor é {}, seu dobro é {}, seu triplo {} e sua raiz quadrada é {:.2f}'.format(value, triple, squareRoot)) """    
#-----------------------------------------------------------------------------

#   Faça um progama que leia notas e depois mostre sua media

""" oneNote = float(input('Digite sua primeira nota: '))
twoNote = float(input('Digite sua segunda nota: '))
avarage = (oneNote + twoNote) / 2
print('Sua média final é de {:.2f}'.format(avarage)) """
#-----------------------------------------------------------------------------

# 
""" def new_func():
    meters = float(input('Uma distância em metros: '))
    km = meters / 1000
    hm = meters / 100
    dam = meters / 10
    dm = meters / 0.1
    cm = meters / 0.01
    mm = meters / 0.001
    print('A media de {}\n{} km\n{} hm\n{} dam\n{:.0f} dm\n{:.0f} cm\n{:.0f} mm'.format(meters, km, hm, dam, dm, cm, mm))

new_func() """

#-----------------------------------------------------------------------------

#   Faça um progama de tabuada

""" tab = int(input('Digite um número para saber sua tabuada: '))
m0 = tab * 0 
m1 = tab * 1
m2 = tab * 2
m3 = tab * 3
m4 = tab * 4
m5 = tab * 5
m6 = tab * 6
m7 = tab * 7
m8 = tab * 8
m9 = tab * 9
m10 = tab * 10
print(f'Seu número é {tab}\n{tab} x 0 = {m0}\n{tab} x 1 = {m1}\n{tab} x 2 = {m2}\n{tab} x 3 = {m3}\n{tab} x 4 = {m4}\n{tab} x 5 = {m5}\n{tab} x 6 = {m6}\n{tab} x 7 = {m7}\n{tab} x 8 = {m8}\n{tab} x 9 = {m9}\n{tab} x 10 = {m10}') """
#-----------------------------------------------------------------------------

#   Faça um progama que real para dolar

""" real = float(input('Qual valor em real você quer converte para dolar, dolar canadense, euro? R$'))
dolar = real / 4.97
dolarCan = real / 3.60
euro = real / 5.26
print('\nO valor do dolar é 4.97, seu valor em dinheiro é {:.2f}, seu dinheiro covertido para dolar é de {:.2f}\n'.format(real, dolar))
print('O valor do dolar Canadense é 3.60, seu valor em dinheiro é {:.2f}, seu dinheiro covertido para dolar Canadense é de {:.2f}\n'.format(real, dolarCan))
print('O valor do euro é 5.26, seu valor em dinheiro é {:.2f}, seu dinheiro covertido para euro é de {:.2f}\n'.format(real, euro)) """
#-----------------------------------------------------------------------------

#   Faça um progama que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

""" width = float(input('Digite a largura de sua parede? '))
height = float(input('Digite a altura da sua parede? '))
area = width * height
tinta = area / 2
print('A area da parede é {:.2f}m². Você perecisará de {:.2f}l de tintas, para pintar sua parede.'.format(area, tinta)) """
#-----------------------------------------------------------------------------

#   Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

""" valueProduct = float(input('Digite o valor do produto? '))  
discount = 0.05
newValue = valueProduct - (valueProduct * discount) 
print(f'O seu produto de R${valueProduct}, irá sair por R${newValue}, com o desconto de 5%.') """
#-----------------------------------------------------------------------------

#   Que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

""" wage = float(input('Digite seu sálario: R$'))
increase = 0.15
valueIncrease = wage * increase
newWage = wage + (wage * increase)
print('Seu aumento foi de R${:.2f}, Seu novo sálario sera de R${:.2f}.'.format(valueIncrease, newWage)) """


#10
""" produto = float(input('Seu produto no pagamento avista terá 7% de desconto, caso parcelado terá 11% de aumento, insira o valor do produto R$'))
avista = 0.07
parcelado = 0.11
valorAvista = produto - (produto * avista)
valorParcelado = produto + (produto * parcelado)
print('Seu produto custará somente R${:.2f} no valor avista, caso pacerlado custará R${:.2f}'.format(valorAvista, valorParcelado)) """
#-----------------------------------------------------------------------------

#11 conversão de °c para °f

""" temp = float(input('Informe a temperatura em °C: '))
fah = (temp * 9 / 5) + 32
print('A temperatura de {:.2f}°C corresponde a {:.1f}°F!'.format(temp,fah)) """
#-----------------------------------------------------------------------------

#12 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

""" dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(total)) """
#-----------------------------------------------------------------------------
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))