# Solicita o valor do produto
valor = float(input("Digite o valor do produto: R$ "))

# Verifica se o valor é maior que 100
if valor > 100:
    desconto = valor * 0.10  # 10% de desconto
    valor_com_desconto = valor - desconto
    print(f"Desconto de 10% aplicado! Valor com desconto: R$ {valor_com_desconto:.2f}")
else:
    print(f"Sem desconto. Valor do produto: R$ {valor:.2f}")
