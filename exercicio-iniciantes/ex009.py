#   Que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

wage = float(input('Digite seu sálario: R$'))
increase = 0.15
valueIncrease = wage * increase
newWage = wage + (wage * increase)
print('Seu aumento foi de R${:.2f}, Seu novo sálario sera de R${:.2f}.'.format(valueIncrease, newWage))