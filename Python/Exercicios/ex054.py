from datetime import date
print('Crie um programa que leia o \033[33m ANO DE NASCIMENTO\033[m de \033[32mSETE PESSOAS\033[m\n'
      'No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.')
print(30*'*-')
maiores = 0
menores = 0
ano = date.today().year
for c in range(0,7):
    p = int(input(f' Em que ano a {c+1}º nasceu? '))
    m = ano - p
    if m >= 17:
        maiores += 1
    else:
        menores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade.')
print(f'E também tivemos {menores} menores de idade.')