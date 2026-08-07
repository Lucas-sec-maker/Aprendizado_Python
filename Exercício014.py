#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para Fahrenheit

#Gerando a entrada de dados 

tempGraus = float(input("Digite a temperatura em Graus Celsius:  "))

#Declarando as variáveis da tranformação
grausFparaC = (tempGraus * 1.8) + 32

#Resultado 
print(f"{tempGraus}C em F é {grausFparaC} ")