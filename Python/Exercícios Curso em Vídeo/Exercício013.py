#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

#Criando o input para entrada dos dados
temperatura = float(input("Diga quantos graus está fazendo na sua região: "))

#definindo o cálculo da transformação.
grausEmF = (temperatura * 1.8) + 32

#Gerando a saída do resultado
print(f"Se na sua região está fazendo {temperatura}º, em F é {grausEmF}º")