def Validar_nome(nome):
    if nome.isalpha():
        return True 
    else: 
        return False 
    
def Validar_idade(idade):
    if idade.isdigit():
        return True 
    else:
        return False 
    
nome = input('Digite seu nome:')
idade = input('Digite sua idade:')  

if Validar_nome(nome):
    print('Nome válido!')
else:
    print('Nome inválido! O nome deve conter apenas letras. ')

if Validar_idade(idade):
    print('Idade válida!')
else:
    print('Idade inválida! A idade deve conter apenas número.')