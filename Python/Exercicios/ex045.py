from random import randint
from time import sleep
print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA\n')
itens = ('   PEDRA   ', '   PAPEL   ', '  TESOURA  ')
jogada = int(input('Qual é sua jogada? '))
pc = randint(0,2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print(15*'-*')

print(' COMPUTADOR ---- JOGADOR ')
print('{}----{}'.format(itens[pc], itens[jogada]))
print(15*'*-')





# PEDRA > TESOURA > PAPEL > PEDRA
#--------------------------------------
if pc == 0: #pedra
    if jogada == 0:
        print('\033[33mEMPATOU!!!')
    elif jogada == 1: #papel
        print('\033[35mVOCÊ GANHOU!!!')
    elif jogada == 2: #tesoura
        print('\033[31mPC GANHOU!!!')
#--------------------------------------
elif pc == 1: #papel
    if jogada == 0:   #pedra
        print('\033[31mPC GANHOU!!!')
    elif jogada == 1: #papel
        print('\033[33mEMPATOU!!!')
    elif jogada == 2: #tesoura
        print('\033[35mVOCÊ GANHOU!!!')
#--------------------------------------
elif pc == 2:#tesoura
    if jogada == 0:#pedra
        print('\033[35mVOCÊ GANHOU!!!')
    elif jogada == 1:#papel
        print('\033[31mPC GANHOU!!!')
    elif jogada == 2:#tesoura
        print('\033[33mEMPATOU!!!')
else:
    print('opção incorreta')