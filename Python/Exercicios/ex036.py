print('\nEscreva um programa para aprovar o empréstimo bancário para a compra de uma casa.'
      '\n Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.'
      '\n A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.')
print(29 * '-=-')

vlcasa = float(input('Digite o valor da casa que deseja comprar: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Digite em quantos anos você pretende parcelar: '))
prestacao = vlcasa / (anos*12)
print(29 * '-=-')
if prestacao > (salario * 30 / 100):
    print('\nPara pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(vlcasa, anos, prestacao))
    print('\033[31mEmprestimo NEGADO!')

else:
    print('\nPara pagar uma casa de R%{:.2f} em {} anos a prestação será de R${:.2f}'.format(vlcasa, anos, prestacao))
    print('\033[34mEmprestimo APROVADO!')
