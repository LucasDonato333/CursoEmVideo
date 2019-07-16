print('Faça um programa que leia o Sexo de uma pessoa, mas só aceite os valores\n'
      'M OU F. Caso esteja errado, peça a digitação novamente até ter um valor correto.')


sexo = str(input('INFORME SEU SEXO: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('INFORME SEU SEXO: [M/F] ')).upper().strip()[0]
print('Dados registrados com sucesso')