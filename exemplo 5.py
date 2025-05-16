Nome = [0] *3
Idade = [0] *3
Telefone = [0] *3
Rua = [0] *3 
Numero = [0] *3
Bairro = [0] *3 
cont = 0
for cont in range(3): 
    print(f'--------{cont + 1}º-Cadastro ------------')
    print()
    print('Digite seu nome:')
    Nome[cont] = input()
    print('Digite a sua idade:')
    Idade[cont] = int(input())
    print('Digite seu telefone:')
    Telefone[cont] = input()
    print('Digite o nome da sua rua:')
    Rua[cont] = input()
    print('Digite o número da sua casa/aptm:')
    Numero[cont] = input()
    print('Digite o nome do bairro:')
    Bairro[cont] = input() 
print('\n' *20) 
for cont in range(3): 
    print(f'Nome: {Nome[cont]}')
    print(f'Idade: {Idade[cont]}')
    print(f'Telefone: {Telefone[cont]}')
    print(f'Rua: {Rua[cont]}')
    print(f'Número: {Numero[cont]}')
    print(f'Bairro: {Bairro[cont]}')
    print('-'*20) 