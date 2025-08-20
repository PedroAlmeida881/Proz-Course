print('Digite o número correspondente ao mês:')
print('''1-Janeiro
2- Fevereiro
3- Março 
4- Abril
5- Maio
6- Junho  
7= Julho 
8- Agosto 
9- Setembro  
10- Outubro  
11-Novembro  
12- Dezembro ''') 

try: 
    numero= int(input('Sua escolha:'))

    match numero:
        case 1: 
         MES = 'Janeiro'
        case 2: 
         MES = 'Fevereiro'
        case 3: 
         MES = 'Março'
        case 4: 
         MES = 'Abril'
        case 5: 
         MES= 'Maio'
        case 6: 
         MES= 'Junho'
        case 7: 
         MES= 'Julho' 
        case 8: 
         MES= 'Agosto'
        case 9: 
         MES= 'Setembro'
        case 10: 
         MES= 'Outubro'
        case 11: 
         MES= 'Novembro'
        case 12: 
         MES= 'Dezembro'      
except ValueError:
      MES = ('Entrada inválida, digite um  número inteiro')

print('O mês selecionado é:', MES)