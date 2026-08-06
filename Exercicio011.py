#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m

#input para altura e largura 

largura = float(input("Largura: "))
altura = float(input("Altura: "))

#calculando as informações
area_parede = altura * largura
litros_tinta = area_parede/2

#Gerando o resultado com as variáveis calculadas
print(f"Sua área para pintura é {largura} x {altura} com área de {area_parede}m²")
print(f"Para pintar a sua parede iremos precisar de {litros_tinta}l de tinta")

