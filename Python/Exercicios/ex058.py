print('Melhore o jogo do DESAFIO #028 onde o computador vai "pensar" em um número entre 0 e 10.\n'
      'Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites\n'
      'foram necessários para vencer.')
#---------------------------------------------------------------------------------------------------------
from random import randint

#Número Random de 0 á 10
n = randint(0,11)
#Definindo Valores
n1 = 12
c = 0
#Mensagem do Robo
print('Sou seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?\n'
      'Qual é seu palpite?\n')
#Enquanto n1 for diferente de n, repita a pergunta
while n1 != n:
    n1 = int(input('Digite seu palpite: '))

    #número de vezes que deu seu palpite
    c = c + 1

    # Se n1 for maior que n - digite um número menor
    if n1 > n:
        print('Menos')
    #Caso seja menor - digite um número maior
    elif n1 < n:
        print('Mais')
print('Acertou')
print('Acertou com {} tentativas. Parabéns'.format(c))


'''
#SOLUÇÃO CURSO EM VIDEO

from random import randint
computador = randint(0, 10)
print('Consegue adivinhar qual número eu pensei?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Teste mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns'.format(palpites))
'''