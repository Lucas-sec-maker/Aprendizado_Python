#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#Gerando o input para o usuário colocar o valor

valor = float(input("Digite o valor em metros: "))

#Gerando as variáveis para calcular a tranformação de metro para o restante.

valorCentimetros = valor * 100
valorMilimetros = valor * 1000

#Gerando a conversão

plural = "Metro" if valor <= 1 else "Metros"
print(f"{valor} {plural} em centímetros é {valorCentimetros} e em milímetros é {valorMilimetros}")