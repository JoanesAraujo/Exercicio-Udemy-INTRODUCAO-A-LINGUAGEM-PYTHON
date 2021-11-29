# -*- coding: latin-1 -*-
# -- LISTA DE EXERCÍCIOS --


# Escreva um programa que receba dois números e um sinal, 
# e faça a operação matemática definida pelo sinal.

resultado = 0
num1 = int(input("Entre com o primeiro número : "))
num2 = int(input("Entre com o segundo número : "))

sinal = input("Escolha operação matemática : ( +,-,* ou /) : ")

if sinal == '+' :
	resultado = num1 + num2
	print('\nO resultado da soma foi : ',resultado)

elif sinal == '-' :
	resultado = num1 - num2
	print('\nO resultado da subtração foi : ',resultado)

elif sinal == '*' :
	resultado = num1 * num2
	print('\nO resultado da multiplicação foi : ',resultado)

elif sinal == '/' :
	resultado = num1 / num2
	print('\nO resultado da divisão foi : {:.0f}'.format(resultado))

else:
	print("Sinal Inválido")