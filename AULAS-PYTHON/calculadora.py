def somar(x,y):
    return x+y    
def subtrair(x,y):
    return x-y   
def multiplicar(x,y):
    return x*y    
def dividir(x,y):  
 if y !=0:  
    return x/y  
 else:
    return"Erro: divisão por zero."
print("Escolha a operação:")
print("1-somar")
print("2-subtrair")
print("3-multiplicar")
print("4-dividir")
op=input("Digite a opção (1/2/3/4):")
num1=float(input("Digite o primeiro número:"))
num2=float(input("Digite o segundo número:"))
if op=="1":
    print("Resultdo", somar(num1,num2))
elif op == "2":
    print("Resultado", subtrair(num1,num2))
elif op == "3":
    print("Resultado", multiplicar(num1,num2)) 
elif op == "4":
    print("Resultado", dividir(num1,num2))
else:
    print("Opção inválida.") 