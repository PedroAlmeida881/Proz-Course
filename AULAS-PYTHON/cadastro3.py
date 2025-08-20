cadastro = []
while True: 
    print('\n1-Adicionar nome\n2 - listar nomes\n3 - sair')
    opção = input('Escolha uma opção:')
    if opção == '1':
        nome = input('Digite o nome:')
        cadastro.append(nome)
        print('Nome cadastro!')

    elif opção == '2': 
        print('\nLista de nomes:')
        for nome in cadastro: 
            print(nome)

    elif opção == '3':
        print('Saindo do programa...')
        break 
    else:
        print('Opção inválida! Tente novamente.')
        