# Função para verificar se o número é um palíndromo
def eh_palindromo(numero):
    # Converte o número para string
    numero_str = str(numero)
    # Verifica se a string é igual à sua reversa
    return numero_str == numero_str[::-1]

# Leitura do número
numero = int(input("Digite um número inteiro: "))

# Verificação e exibição do resultado
if eh_palindromo(numero):
    print(f"O número {numero} é um palíndromo!")
else:
    print(f"O número {numero} não é um palíndromo.") 