# -*- coding: latin-1 -*-
# -- LISTA DE EXERCÍCIOS --


# Faça um programa que receba duas notas digitadas pelo usuário. 
# Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.

nota1 = float(input("Entre com a 1a nota: "))   
nota2 = float(input("Entre com a 2a nota: "))

total=0

media = (nota1 + nota2)/2

if media >= 6:
 	print("você foi aprovado")
else:
	print("Você foi reprovado")
