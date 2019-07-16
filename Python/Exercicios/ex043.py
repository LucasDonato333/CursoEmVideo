print('Desenvolva uma lógica que leia o peso e a altura de uma pessoa,'
      '\ne a altura de uma pessoa, calcule seu \033[1;34mIMC\033[m e mostre seu status,\n'
      ' de acordo com a tabela abaixo:\n\n'
      '|- Abaixo de 18.5: Abaixo do Peso|\n'
      '|- Entre 18.5 e 25: Peso ideal   |\n'
      '|- Entre 25 até 30: Sobrepeso    |\n'
      '|- Entre 30 até 40: Obesidade    |\n'
      '|- Acima de 40: Obesidade Mórbida|\n\n')

# Calculo imc= peso/altura*altura

peso = float(input('Peso   |'))
altura = float(input('Altura |'))
imc = peso / (altura ** 2) # ** Potencia

if imc <= 18.5:
    print('Abaixo do Peso')

elif imc > 18.5 and imc <= 25:
    print('Peso Ideal')

elif imc >25 and imc <=30:
    print('Sobrepeso')

elif imc >30 and imc <=40:
    print('Obesidade')

elif imc >40:
    print('Obesidade Mórbida')

else:
    print('')