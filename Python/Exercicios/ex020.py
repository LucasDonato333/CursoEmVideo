print('O mesmo professor do desafio\nanterior que sortear a ordem\nde apresentação de trabalhos\ndos alunos. Faça um programa\nque leia o nome dos quatro\nalunos e mostre a ordem sorteada.')
print(35 * '-')

import random

n1 = input('Nome: ')
n2 = input('Nome: ')
n3 = input('Nome: ')
n4 = input('Nome: ')

lista = [n1, n2, n3, n4]

random.shuffle(lista)
print(lista)
