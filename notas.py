# Programa para verificar se o aluno passou

nota = float(input('Digite a nota (0 a 10):')) 
while nota < 0 or nota > 10:
    print('Erro! A nota deve ser entre 0 a 10')
    nota = float(input('Digite a nota novamente:'))
if nota >= 7:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')