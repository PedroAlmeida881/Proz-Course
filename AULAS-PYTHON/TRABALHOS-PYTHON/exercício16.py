#Classificação de Idade:
idade = int(input('Digite sua idade:'))

if idade < 0:
    print('Idade inválida.')
elif idade <= 2:
    print('Bebê')
elif idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 29:
    print('Adulto Jovem') 
elif idade <= 59:
    print('Adulto')
else:
    print('Velho')