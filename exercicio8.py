# Cria uma lista vazia para armazenar os números
numeros = []

# Solicita ao usuário 4 números
for i in range(4):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Conta quantos números são negativos
quantidade_negativos = 0
for num in numeros:
    if num < 0:
        quantidade_negativos += 1

# Exibe o resultado
print(f"\nVocê digitou {quantidade_negativos} número(s) negativo(s).")
