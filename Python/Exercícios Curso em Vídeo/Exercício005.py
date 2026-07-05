#Faça um programa que leia um número inteiro e mostre seu sucessor e antecessor.

#criando o input para entrada de dados.
while True:
    try:
        numero = int(input("Digite um número: "))

            #criando as variáveis sucessor e sucessor do número digitado pelo usuário.
        sucessor = numero + 1
        antecessor = numero - 1

            #processando as informações
        print(int(input(f"O seu número é {numero}. Seu sucessor é {sucessor} e seu antecessor é {antecessor}")))
            
    except ValueError: 
                #Se o usuário digitar algo que não seja número, o Python vem aqui.
            print("Erro: Por favor, digite apenas números inteiros (ex: 1, 2, 3).")
    except Exception as erro:
            
            print(f"Ocorreu um erro inesperado: {erro}")
