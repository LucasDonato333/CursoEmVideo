print('Escreva um programa que leia dois números\n'
      'mostrando na tela uma mensagem: \n'
      '- O primeiro valor é maior\n'
      '- O segundo valor é maior\n'
      '- Não existe valor maior, os dois são iguais\n')
n = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

if n > n2:
    print('O primeiro valor é maior')
elif n < n2:
    print('O segundo valor é maior')
else:
    print('Os dois valores são IGUAIS')