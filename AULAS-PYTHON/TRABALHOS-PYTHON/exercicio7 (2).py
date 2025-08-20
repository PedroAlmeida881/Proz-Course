# Solicita os valores do usuário
valor1 = input("Digite o primeiro valor: ")
valor2 = input("Digite o segundo valor: ")

# Exibe os valores originais
print(f"\nAntes da troca:\nValor 1 = {valor1}\nValor 2 = {valor2}")

# Troca os valores
valor1, valor2 = valor2, valor1

# Exibe os valores trocados
print(f"\nDepois da troca:\nValor 1 = {valor1}\nValor 2 = {valor2}") 
