print('Um professor quer sortear\num dos seus quatro alunos\npara apagar o quadro.\n'
'\n Faça um programa que\najude ele, lendo o nome\ndeles e escrevendo o nome\ndo escolhido')
print('------------------------------')

import random

n1 = input('Nome do Aluno: ')
n2 = input('Nome do Aluno: ')
n3 = input('Nome do Aluno: ')
n4 = input('Nome do Aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O Aluno escolhido para apagar a lousa foi {}'.format(escolhido))

