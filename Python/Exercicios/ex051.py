print('Desenvolva um programa que leia o primeiro termo e a razão de uma PA.\n'
      'No final, mostre os 10 primeiros termos dessa progressão.\n')


pri= int(input('PRIMEIRO TERMO: '))
r= int(input('RAZÃO: '))
d = pri + (10 - 1) * r
for c in range(pri,d + r,r):
    print(c,end=' -> ')
print('Acabou')