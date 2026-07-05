#Ler o cateto oposto e o adjacente para calcular a hipotenusa 

catetO = float(input("Qual é o cateto oposto do triângulo? "))
catetA = float(input("Qual é o cateto adjacente do triângulo? "))

#variáveis do triângulo

hipotenusa = ((catetO ** 2) + (catetA ** 2)) ** 0.5

#resultado final

print(f"A hipotenusa de um triâgulo com cateto Oposto de {catetO} e cateto adjacente {catetA} é  {hipotenusa:.2f}")