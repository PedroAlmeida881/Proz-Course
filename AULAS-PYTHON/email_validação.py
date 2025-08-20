import re

regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

email = input('Digite seu email para validação: ')

if re.match(regex, email):
    print("\u2705 E-mail válido!")
else:
    print("\u274C E-mail inválido, tente novamente.")
