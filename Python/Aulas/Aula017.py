#Exemplo Lanche
'''
lanche = ['hamburguer','suco','pizza','pudim']
print(lanche)
lanche[3]='picolé'#realiza a troca de elementos
print(lanche)
lanche.append('Coockie')#adiciona um elemento
print(lanche)
lanche.insert(0,'cachorro quente')#adciona um elemento antes de hamburguer
print(lanche)

#eliminando itens


del lanche[3]#Comando (del)
lanche.pop(3)#Método (pop)

lanche.remove('pizza')#Método (remove)
print(lanche)

if 'pizza' in lanche
    lanche.remove(pizza)

'''

#Exemplo Range
'''
valores = list(range(0,11))
print(valores)
'''

#Exemplo Valores
'''
valores = [8,2,5,4,9,3,0]
valores.sort()#ordena valores
valores.sort(reverse=True)#inverte ordem
print(len(valores))
print(valores)
'''

#Exemplo Frutas
'''
frutas = ['laranja','banana','maçã']
print(frutas)
frutas.sort()
frutas.sort(reverse = True)
frutas.append('morango')
frutas.insert(3,'abacaxi')
frutas.pop(3)
frutas.remove('morango')

if 'cana' in frutas:
    frutas.remove('cana')
else:
    print('Não existe essa fruta')
    
print(frutas)

print(f'essa lista tem {len(frutas)} elementos')
num = [2, 5, 9, 1]

'''

# Recebendo valores para adcionar em uma lista
'''
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Acabou')
'''

# Copiando lista
'''
a = [2, 3, 4, 7]
b = a[:] # Recebe a cópia dos valores
b = a   #faz um ligação entre as listas, fazendo com que a mudança de uma seja a mudança da outra
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''