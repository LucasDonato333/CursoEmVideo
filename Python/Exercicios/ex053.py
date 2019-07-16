#Recebe a frase, retira espaços(antes e depois), deixa em letra maiuscula.
frase = str(input('Digite uma frase: ')).strip().upper()
#Dividi por espaços, tornando um "lista"
palavras = frase.split()
#Junta todas as palavras em um strig só.
junto = ''.join(palavras)

#fatiamento
inverso = junto[::-1]


#Compara "JUNTO" com "INVERSO"
if junto == inverso:
    print(f'{inverso} é palíndromo!!!')
else:
    print(f'{inverso} não é palíndromo')