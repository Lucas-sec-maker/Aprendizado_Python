#Lê o cateto oposto e o adjacente de um triângulo retângulo, e calcula e mostra a hipotenusa.

catetoA = float(input("Digite o valor do cateto Adjacente : "))
catetoO = float(input("Digite o valor do cateto Oposto: "))

#Variável do calculo

hipotenusa = (catetoA**2 + catetoO**2) ** 0.5

#Resultado
print(f"O valor da hipotenusa é {hipotenusa}")