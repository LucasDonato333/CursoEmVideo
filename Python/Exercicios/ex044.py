print('Elabore um programa que calcule o valor a ser pago por um produto, \n'
      'considerando o seu \033[36m preço normal \033[me\033[35m \033[36mcondição de pagamento\033[m:\n'
      '- À vista\033[36m dinheiro/cheque\033[m: \033[35m10% de desconto \033[m \n'
      '- À vista no\033[36m cartão\033[m: \033[35m5% de desconto \033[m \n'
      '- Em até\033[36m 2x no cartão\033[m: \033[35mpreço normal \033[m \n'
      '- Em\033[36m 3x ou mais no cartão\033[m: \033[35m20% de juros \033[m \n')
#-------------------------------------------------

print(30*'-=-')
print('\n')

#-------------------------------------------------

print(11*'===', end='')
print(' LOJA DO DONATO ', end='')
print(11*'===', end='\n\n')

#-------------------------------------------------

pagamento = float(input('Preço das compras: R$ '))
d10 = (pagamento * 10)/100
d5 = (pagamento * 5)/100
d2 = (pagamento / 2)
d3 = (pagamento * 20)/100
#-------------------------------------------------

print('\nFormas de pagamento\n')

#-------------------------------------------------

print('[ 1 ] à vista dinheiro/cheque\n'
      '[ 2 ] à vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão\n')

#-------------------------------------------------

#O = Operação

o = int(input('Opção de pagamento: '))

#-------------------------------------------------
# IF escolha de pagamento

if o == 1:
    print(30 * '-*-')
    print('\033[36m[ 1 ] à vista dinheiro/cheque\033[m\n'
      '[ 2 ] à vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão\n')
    print(30 * '-*-')
    print('Valor total com \033[31m 10%\033[m de DESCONTO')
    print('R${:.2f}'.format(pagamento - d10))

elif o == 2:
    print(30 * '-*-')
    print('[ 1 ] à vista dinheiro/cheque\n'
          '\033[36m[ 2 ] à vista cartão\033[m\n'
          '[ 3 ] 2x no cartão\n'
          '[ 4 ] 3x ou mais no cartão\n')
    print(30 * '-*-')
    print('Valor total com \033[31m5%\033[m de DESCONTO')
    print('R${:.2f}'.format(pagamento - d5))
elif o == 3:
    print(30 * '-*-')
    print('[ 1 ] à vista dinheiro/cheque\n'
          '[ 2 ] à vista cartão\n'
          '\033[36m[ 3 ] 2x no cartão\033[m\n'
          '[ 4 ] 3x ou mais no cartão\n')
    print(30 * '-*-')
    print('Valor total \033[31m2x sem juros\033[m de {:.2f}.'.format(d2))

elif o == 4:
    print(30 * '-*-')
    print('[ 1 ] à vista dinheiro/cheque\n'
          '[ 2 ] à vista cartão\n'
          '[ 3 ] 2x no cartão\n'
          '\033[36m[ 4 ] 3x ou mais no cartão\033[m\n')
    print(30 * '-*-')

    nparc = int(input('Digite o número de parcelas desejadas.'
                      '\n(MÁXIMO DE 12x)\n'
                      ''))

    if  nparc >= 3 and nparc <=12:
        print('\n')
        total = (pagamento + d3 )

        print('O valor a ser pago \n'
          '\033[31m{}x \033[mde \033[31mR${:.2f}\033[m\n'
          'TOTAL | \033[31mR${:.2f}\033[m com \033[31m20% de juros.\033[m |\n'.format(nparc, total/nparc, total))
        print(30*'-*-')
    else:
        print('\033[31mNÚMERO DE PARCELAMENTO INCORRETO!!!!\033[m')
else:
    print('Opção incorreta!!!')
#-------------------------------------------------


