#crie um programa que quanto dinheiro ela tem na carteira e mostre quanto de dólar ela pode comprar.

#declarando o input do usuário 

carteira = float(input("Digite o valor que você tem na carteira : "))

#variável que converte em dólar

real_dolar = carteira / 5.01

plural = "Dólar" if real_dolar <= 1 else "Dólares"

print(f"Com ${carteira} reias você consegue comprar US{real_dolar} {plural}")
