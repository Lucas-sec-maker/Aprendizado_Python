#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

#Gerando o input para o preço do produto.
preço = float(input("Digite aqui o preço do seu produto: "))

#declarando o calculo do desconto
desconto = (preço * 5)/100
preço_desconto = preço - desconto

#Gerando a saída com o preço e o desconto
print(f"Seu produto de ${preço} reais , com 5% de desconto vai sair por ${preço_desconto}")

