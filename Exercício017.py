#Programa que lê um ângulo qualquer e mostre o valor do seno, seno, cosseno e tangente do ângulo.
import math

angulo = float(input("Digite o ângulo do triângulo : "))

#Transformando em rad
angulo_radiano = math.radians(angulo)

#Definindo as variáveis seno,cosseno e tangente
seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)