print('Desenvolva um programa que leia seis números inteiros e mostre a soma\n'
      'apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.\n')

total = 0
for cont in range(1,7):
    num = int(input('Digite o número: '))
    par = num % 2

    if par == 0:
        total = total + num
    else:
        print('Não é par')
print('A soma dos números pares é {}'.format(total))