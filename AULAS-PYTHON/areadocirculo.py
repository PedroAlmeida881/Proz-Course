#Função para calcular a área de um circulo
import math
def calcular_area_circulo(raio):
    # Fórmula para calcular a área do circulo:
    area = math.pi * (raio ** 2)
    return area
    # Leitura do raio
   
raio = float(input('Digite o raio do círculo: '))
# Chamada da função e exibição do resultado
print(f'A área do círculo com raio {raio} é: {calcular_area_circulo(raio)}')