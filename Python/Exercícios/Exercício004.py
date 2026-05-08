#Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo
#  e todas as informações possiveis sobre ele

valor = input("Digite algo: ")

print("O tipo primitivo desse valor é ", type(valor))
print("Só tem espaços? ", valor.isspace())
print("É um número?", valor.isnumeric())
print("É alfanumérico? ", valor.isalnum())
print("Está em maiusculas? ", valor.isupper())
print("Está em minusculas?", valor.islower())
print("Está capitalizada?",valor.istitle())