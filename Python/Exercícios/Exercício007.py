#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

#Gerando o input para o aluno colocar suas notas
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota : "))

#declarando a variável que irão servir de cálculo.
mediaNota =(nota1 + nota2)/2

#Resultado.
print(f"Então sua primeira nota é {nota1} e a segunda é {nota2} ? Sua média é {mediaNota}")

