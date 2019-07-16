print('''
Escreva um programa que leia um número inteiro qualquer e
peça o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal''')
print(25 * '-=-')
n = int(input('Digite um valor: '))
print('''\nEscolha uma opção
\033[32m[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL\033[m''')
o = int(input('Opção : '))
print('O número {} convertido para'.format(n))

if o == 1:
    print('BINÁRIO = {}'.format(bin(n)[2]))

elif o == 2:
    print('OCTAL = {}'.format(oct(n)[2]))

elif o == 3:
    print('HEXADECIMAL = {}'.format(hex(n)[2]))
else:
    print('Opção incorreta.')