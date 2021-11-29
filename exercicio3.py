# -*- coding: latin-1 -*-
# -- LISTA DE EXERCÍCIOS --


# Escreva um programa que resolva uma equação de segundo grau.  
import math
a = 1
b = -10
c = 24
x1 = 0
x2 = 0

delta = (b ** 2) - (4 * a * c)
print (delta)

x1 = ( - b + math.sqrt(delta)) / (2 * a)
print(f'O resultado de X1 é : {x1:.0f}')
x2 = ( - b - math.sqrt(delta)) / (2 * a)
print(f'O resultado de X2 é : {x2:.0f}')

print ('\nAs minhas raízes da equação do 2o grau são ({:.0f} e {:.0f})' .format(x1,x2))
