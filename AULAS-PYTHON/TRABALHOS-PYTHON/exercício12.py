# Solicita a nota do aluno
nota = float(input("Digite a nota do aluno (de 0 a 10): "))

# Verifica se a nota está dentro do intervalo válido
if 0 <= nota <= 10:
    # Verifica aprovação
    if nota >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado.")
else:
    print("Nota inválida. Digite um valor entre 0 e 10.")
