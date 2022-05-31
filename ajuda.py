import math
print('')
print('Olá, essa mini calculadora foi desenvolvida por LealzimSTK')
print('Está simples, pois eu não manjo muito de Python')
print('Porém com o tempo irei aprimora-la')
print('')
print('O que você deseja calcular?')
print("""
1) Adição
2) Subtração
3) Multiplicação
4) Divisão
5) Raiz Quadrada
6) Raiz Cúbida
7) Catetos
8) Calculo de ângulos (Trigonometria)""")
print('')
respuser = int(input('>>'))
if respuser == 1:
    print('Primeiro valor:')
    n1 = int(input('>'))
    print('Segundo valor:')
    n2 = int(input('>'))
    soma = n1+n2
    print('{}+{}={}'.format(n1, n2, soma))
elif respuser == 2:
    print('Primeiro valor:')
    n1 = int(input('>'))
    print('Segundo valor:')
    n2 = int(input('>'))
    sub = n1-n2
    print('{}-{}={}'.format(n1, n2, sub))
elif respuser == 3:
    n = int(input('Digite um valor: '))
    print('{:<2}x{:>2} = {:>1}'.format(n, 1, n*1))
    print('{:<2}x{:>2} = {:>1}'.format(n, 2, n*2))
    print('{:<2}x{:>2} = {:>1}'.format(n, 3, n*3))
    print('{:<2}x{:>2} = {:>1}'.format(n, 4, n*4))
    print('{:<2}x{:>2} = {:>1}'.format(n, 5, n*5))
    print('{:<2}x{:>2} = {:>1}'.format(n, 6, n*6))
    print('{:<2}x{:>2} = {:>1}'.format(n, 7, n*7))
    print('{:<2}x{:>2} = {:>1}'.format(n, 8, n*8))
    print('{:<2}x{:>2} = {:>1}'.format(n, 9, n*9))
    print('{:<2}x {:>2} = {:>1}'.format(n, 10, n*10))
elif respuser == 4:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print('A resposta é: {}'.format(n1/2))
elif respuser == 5:
    n1 = int(input('Digite um número: '))
    print('A raiz quadrada de {} é {:.2f}'.format(n1, n1**(1/2)))
elif respuser == 6:
    n1 = int(input('Digite um número: '))
    print('A raiz quadrada de {} é {:.2f}'.format(n1, n1**(1/3)))
elif respuser == 7:
    cateto_oposto = float(input('Comprimento do cateto oposto: '))
    cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
    hi = math.hypot(cateto_oposto, cateto_adjacente)
    print('A hipotenusa vai medir {:.2f}'.format(hi))
elif respuser == 8:
    angulo = int(input('Digite o ângulo que você deseja: '))
    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    tangente = math.tan(math.radians(angulo))
    print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
    print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
    print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
else:
    print('Error !')
