#Solicita ao usuário o número inicial e final
numero_inicial = int(input('Digite o nýmero inicial:'))
numero_final = int(input('Digite o número final:'))

#Verifica se o número inicial é menor que o número final
if numero_inicial <= numero_final:
    for numero in range(numero_inicial, numero_final + 1):
        print(numero)
else:
    print('O número inicial deve ser menor ou igual ao número final.')