Nome = [0] *3
Idade = [0] *3
cont = 0
for cont in range(3): 
    print(f'--------{cont + 1}º-Cadastro ------------')
    print()
    print('Digite seu nome:')
    Nome[cont] = input()
    print('Digite a sua idade:')
    Idade[cont] = int(input())
print('\n' *20) 