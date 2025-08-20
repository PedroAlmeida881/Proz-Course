# Pede o valor do produto
valor = float(input("Digite o valor do produto: R$ "))

# Pede o percentual de desconto
desconto = float(input("Digite o percentual de desconto (%): "))

# Calcula o valor do desconto
valor_desconto = valor * (desconto / 100)

# Calcula o valor final com desconto
valor_final = valor - valor_desconto

# Mostra o resultado
print(f"O valor com desconto é: R$ {valor_final:.2f}")