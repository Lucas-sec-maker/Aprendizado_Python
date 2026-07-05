#Escreva um programa que pergunte a quantidade de Km percorridos por um carro 
#alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


#Gerando os inputs para informação.
KmPercorrido = float(input("Quantos Kms foi percorrido?: "))
Qt_dias_aluguel = int(input("Quantos dias foi utilizado o carro?: "))

#Métricas para calcular os valores : 0.15 por km e 60 por dia
valorTotal = (KmPercorrido * 0.15) + (Qt_dias_aluguel * 60)

#Gerando a saída com as informações.
print(f"O valor total a pagar será ${valorTotal}")
