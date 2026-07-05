#Crie um programa que leia um número REAL qualquer
#pelo teclado e mostre na tela a sua porção inteira
import math

entrada = float(input("Digite um número: "))
inteiro = math.trunc(entrada)

print(f"A parte inteira de {entrada} é {inteiro}")


