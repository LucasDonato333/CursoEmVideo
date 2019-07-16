print('Refaça o DESAFIO 035 dos triangulos, acrescentando o recurso de\n'
      'mostrar que tipo de triângulo será formado:\n'
      '- [\003EQUILÁTERO: Todos os lados iguais\n'
      '- ISÓSCELES: Dois lados iguais\n'
      '- ESCALENO: Todos os lados diferentes\n')

l1 = int(input('PRIMEIRO SEGMENTO | '))
l2 = int(input('SEGUNDO SEGMENTO  | '))
l3 = int(input('TERCEIRO SEGMENTO | '))

if l1 < l2 + l3 and l2 < l1 +l3 and l3 < l1 + l2:
      print('Podem formar um triangulo ', end='')#end='' vai eliminar o enter e trazer a palavra a baixo, seguida da frase
      if l1 == l2 == l3:
            print('EQUILÁTERO.')

      elif l1 == l2 or l1 == l3 or l2 == l3:
            print('ISÓSCELES.')

      else:
            print('ESCALENO.')
else:
      print('Não podem formar um Triângulo.')
