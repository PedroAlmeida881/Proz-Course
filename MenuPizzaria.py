#Menu de uma pizzaria

print("Pizzaria del primo - Seja bem vindo!")
print("---Cardápio - preços---")
print(" ")
print("***** Pizzas - sabores********")
print(" BOLANHESA, PEPERONI, PORTUGUESA")
print("*****Pizzas - Sabores*********")
print(" Pizza pequena R$ 10,00 ")
print(" Pizza Média R$ 15,00  ") 
print(" Pizza Grande R$ 20,00  ")
print("*******Refrigerantes********")
print(" Coca-cola 500 ML     R$ 7,00  ")
print(" Guaraná  500 ML     R$ 6,00  ")
print(" Fanta    500 ML     R$ 5,00  ")
print("-"*60)
print(" ")
print("Faça o seu pedido para pizza:")
print("1- Bolonhesa")
print("2- Peperoni")
print("3- Portuguesa")
print("-"*60)

pedidopizza= int(input())

print("Digite o tamanho da pizza:")
print("P - pequena")
print("M - Média")
print("G - Grande")
print("-"*60)

tampizza= input().upper()

print("Faça seu pedido para refrigerante:")
print("1- Coca-cola")
print("2- Guaraná")
print("3- Fanta")
print("-"*60)

pedidorefri = int(input()) 

if (pedidopizza == 1) and (tampizza == "P") and (pedidorefri ==1):
    precopagar = 10.00 + 7.00 
    pedidos = "Bolonhesa, Pequena, Coca-cola"

elif (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10.00 + 6.00 
    pedidos = "Bolonhesa, Pequena, Guaraná"   

elif (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 10.00 + 5.00 
    pedidos = "Bolonhesa, Pequena, Fanta" 

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 15.00 + 7.00 
    pedidos = "Bolonhesa, Média, Coca-cola" 

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.00 + 6.00 
    pedidos = "Bolonhesa, Média, Guaraná" 

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 15.00 + 5.00
    pedidos = "Bolonhesa, Média, Fanta" 

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.00 + 7.00 
    pedidos = "Bolonhesa, Grande, Coca-cola"

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.00 + 6.00 
    pedidos = "Bolonhesa, Grande, Guaraná "

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 20.00 + 5.00 
    pedidos = "Bolonhesa, Grande, Fanta"

elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 10.00 + 7.00 
    pedidos = "Peperoni, Pequena, Coca-cola"

elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 10.00 + 7.00 
    pedidos = "Portuguesa, Pequena, Coca-cola"

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 15.00 + 7.00 
    pedidos = "Peperoni, Média, Coca-cola"

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 15.00 + 7.00 
    pedidos = "Portuguesa, Média, Coca-cola" 

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.00 + 7.00 
    pedidos = "Peperoni, Grande, Coca-cola"

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.00 + 7.00 
    pedidos = "Portuguesa, Grande, Coca-cola" 

elif (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10.00 + 6.00 
    pedidos = "Bolonhesa, Pequena, Guaraná"

elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10.00 + 6.00 
    pedidos = "Peperoni, Pequena, Guaraná"

elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10.00 + 6.00 
    pedidos = "Portuguesa, Pequena, Guaraná"

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.00 + 6.00 
    pedidos = "Bolonhesa, Média, Guaraná" 

elif (pedidopizza ==2) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.00 + 6.00 
    pedidos = "Peperoni, Média, Guaraná"

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.00 + 6.00 
    pedidos = "Portuguesa, Média, Guaraná" 

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.00 + 6.00 
    pedidos = "Bolonhesa, Grande, Guaraná" 

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.00 + 6.00 
    pedidos = "Peperoni, Grande, Guaraná" 

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.00 + 6.00 
    pedidos = "Portuguesa, Grande, Guaraná" 

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 15.00 + 5.00 
    pedidos = "Peperoni, Média, Fanta" 

elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 10.00 + 5.00 
    pedidos = "Peperoni, Pequena, Fanta" 

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 15.00 + 5.00 
    pedidos = "Portuguesa, Média, Fanta" 

elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 10.00 + 5.00 
    pedidos = "Portuguesa, Pequena, Fanta" 
else:
    print("Pedido inválido. Verifique os dados digitados.")
    exit()
print(f"O preço foi R$ {precopagar:.2f} e seu pedido foi: {pedidos}")