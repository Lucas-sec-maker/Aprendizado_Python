#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

#Gerando a entrada para o usuário
salario = float(input("Digite seu salário atual: "))

#Criando as variáveis para o cálculo

aumento = salario + (salario * 0.15)

#Resultado

print(f"Parabéns pelo aumento! Seu salário com 15% de aumento agora é ${aumento}")
