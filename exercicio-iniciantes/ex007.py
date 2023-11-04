#   Faça um progama que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

width = float(input('Digite a largura de sua parede? '))
height = float(input('Digite a altura da sua parede? '))
area = width * height
tinta = area / 2
print('A area da parede é {:.2f}m². Você perecisará de {:.2f}l de tintas, para pintar sua parede.'.format(area, tinta))