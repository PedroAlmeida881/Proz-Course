letra = input('Digite uma letra:').upper()

if letra in ('A', 'E', 'I', 'O', 'U'):
    print('Sua letra é uma vogal!')
elif letra.isalpha() and len(letra) == 1:
    print('Sua letra é uma consoante.')
else:
    print('Erro, digite apenas uma letra!')
