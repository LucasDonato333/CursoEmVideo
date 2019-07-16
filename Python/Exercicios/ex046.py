print('Faça um programa que mostre na tela uma \033[34mCONTAGEM REGRESSIVA\033[m\n'
      'para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de\n'
      '\033[34m1 SEGUNDO\033[m entre eles.\n')
print(30*'-*')

from time import sleep
for c in range(10,-1,-1):#DE 10 há -1 subtraindo 1.
    print('{} {} {}'.format(c*'*',c,c*'*'))
    sleep(1)
print('\033[32m********BUM********')
sleep(0.15)
print('\033[31m********BUM********')
sleep(0.10)
print('\033[35m*******CABUM*******')