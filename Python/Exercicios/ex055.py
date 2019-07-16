cor = '\033[31m'
scor = '\033[m'
print(f'Faça um programa que leia o {cor}PESO{scor} cinco pessoas.\n'
      f'No final, mostre qual foi o {cor}MAIOR{scor} e o {cor}MENOR{scor} pesso lidos.')
print(30*'~-')
maior = 0
menor = 0

for pessoa in range(1,6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior = menor = pessoa
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior} Kg')
print(f'O menor pessoa lido foi de {menor} Kg')