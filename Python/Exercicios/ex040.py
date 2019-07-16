print('\nCrie um programa que leia duas notas de um aluno e calcule sua média,\n'
      'mostrando uma mensagem no final, acordo com a média atingida:\n'
      '- Média abaixo de 5.0: REPROVADO\n'
      '- Média entre 5.0 e 6.9: RECUPERAÇÃO\n'
      '- Média 7.0 ou superior: APROVADO\n')
print(30*'-=-')
print('\n')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('DIgite a segunda nota: '))
media = (n1 + n2) / 2

if media > 7:
    print('Sua média é {}\n APROVADO'.format(media))
elif media >4.1 and media < 7:
    print('Sua média é {}\n RECUPERAÇÃO'.format(media))

else:
    print('Sua média é {}\n REPROVADO'.format(media))