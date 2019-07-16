r = 0
contador = 0
for c in range(1,501,2):
    if c % 3 == 0:
        contador += 1#MESMA COISA QUE (CONTADOR = CONTADOR + 1)
        r = r + c


print('A soma dos {} valores solicitadors é {}'.format(contador,r))