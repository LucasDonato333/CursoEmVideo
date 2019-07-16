print('Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.\n'
      'No final, mostre qual foi o maior e menor valor digitado e as suas \n'
      'respectivas posições na lista')

valores = []
maior = 0
menor = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))#cont +1
    if cont == 0:
        maior = menor = valores[0]
    else:
        if valores[cont] > maior:
           maior = valores[cont]
        if valores [cont] < menor:
            menor = valores[cont]

print(f'Você digitou os valores {valores}')
print(f'Maior valor {maior} na posição {maior[cont]}')
print(f'Menor {menor} na posicação {menor[cont]}')