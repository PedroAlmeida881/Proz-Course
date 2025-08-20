#Calculadora de juros simples:
principal=float(input('Digite o valor principal:'))
taxadejuros=float(input('Digite o valor da taxa de juros em (%):'))
anos=int(input('Digite o número de anos:'))
Montante = principal + (principal * taxadejuros * anos / 100) 
print('O resultado é:',principal,taxadejuros,anos)