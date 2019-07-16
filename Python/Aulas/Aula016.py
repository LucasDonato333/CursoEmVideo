#Variáveis Compostas
# (Tuplas)

#   -------- As tuplas são IMUTÁVEIS --------
'''
lanche = ('Hambúrhuer', 'Suco', 'Pizza', 'Pudim', 'Batata')
print(lanche[:2])
for pos, comida in enumerate (lanche):
    print('Eu vou comer {}na posição {}'.format(comida,pos))
#OU

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print(sorted(lanche))
print('Comida pra caralho')
'''
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))#Quantas vezes aparece
print(len(c))#Quantos dados há nas tuplas
print(c.index(5))#resultado seria 0 pois é a primeira ocorrencia.
print(c.index(5,1))#número 5 apartir da posição 1
'''
