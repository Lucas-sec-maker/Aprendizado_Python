#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua taboada

#Gerando o input para o usuário colocar o número.

numero = int(input("Digite um número: "))

#Gerando o cálculo da taboada.

contador = 0
multiplicador = 1

print("====================")
while (contador <= 10 and multiplicador <= 10):
    taboada = numero * multiplicador
    print(f"{numero} x {multiplicador} = {taboada}")

    contador+=1
    multiplicador+=1
    
   

print("====================")