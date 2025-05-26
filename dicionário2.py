alunos= {}

nomes = ['Ana', 'Carlos', 'Maria', 'Felipe',]

for nome in nomes:
    idade = input(f'Digite a idade de {nome}:')
    alunos[nome] = idade 
    print('\n Lista de alunos:')
    for nome,idade in alunos.items(): 
        print(f'{nome}: {idade} anos')