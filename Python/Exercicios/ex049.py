print('Refaça o \033[94mDESAFIO #009\033[m, mostrando a \033[94mTABUADA\033[m de um número\n'
      'que o usuário ecolher, só que agora utilizando um \033[94mLAÇO FOR\033[m.\n')

n1 = 0
n2 = int(input('N: '))
print(30*'*')

for n1 in range(0,11):
    r = n1 * n2
    print('{}X{}={}'.format(n1, n2, r))
print(30*'*')