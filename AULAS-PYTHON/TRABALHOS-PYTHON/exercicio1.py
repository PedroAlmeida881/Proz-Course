print('Seja bem-vindo a cafeteria del primo')
valor_cafe = float(input("Qual é o valor de um café? R$ "))

quantidade = int(input("Quantos cafés você quer comprar? "))

total = valor_cafe * quantidade

print(f"Você deve pagar R$ {total:.2f}")