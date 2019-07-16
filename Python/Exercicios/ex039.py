from datetime import date

print('Faça um programa que leia o ano de nascimento de uma jovem e informe,\n'
      'de acordo com sua idade, se ele ainda vai se alistar ao serviço militar\n'
      'se é a hora de se alistar ou seja ja passou do tempo do alistamento.\n'
      'Seu programa tambem deverá msotrar o tempo que falta ou que passou do prazo\n')

print(30*'-=-')
print('\n')

nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc


print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano))

if idade < 18:
    f = 18 - idade
    print('Você irá se alistar em {} daqui á {} anos'.format((f + ano), 18 - idade))
elif idade > 18:
    f = idade - 18
    print('Você já se alistou em {}, cerca de {} anos atrás'.format((ano - f),f))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
