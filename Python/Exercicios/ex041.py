from datetime import date
print('A Confederação Nacional de Natação precisa de um programa que leia\n'
      'o ano de nascimento de um atleta e mostre sua categoria, de acordo\n'
      'com a idade:\n'
      '- Até 9 anos: MIRIM\n'
      '- Até 14 anos: INFANTIL\n'
      '- Até 19 anos: JUNIOR \n'
      '- Até 25 anos: SÊNIOR\n'
      '- Acima: MASTER\n')
print(30*'-=-')
print('\n')

n = int(input('Digite o ano de nascimento do atleta: '))
print('\n')
atual = date.today().year
idade = atual - n
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
      print('CATEGORIA MIRIM')
elif idade <= 14:
      print('CATEGORIA INFANTIL')
elif idade <= 19:
      print('CATEGORIA JUNIOR')
elif idade <= 25:
      print('CATEGORIA SÊNIOR')
else:
      print('CATEGORIA MASTER')