#Bruna Ribeiro

import math

graus = float(input())
n = int(input())
cont = 1
x = (float(math.radians(graus)))

cont1 = 1
cont2 = 0
conts = 1
soma1 = 0
soma2 = 0
exp1 = 0
expo2 = 0

while cont <= n:
    cont = cont + 1
    exp1 = x ** cont1 
    expo2 = x ** cont2
    rad1 = (math.factorial(cont1))
    rad2 = (math.factorial(cont2))
    dsen = (exp1 / rad1) 
    dcos = (expo2 / rad2)
    conts = conts + 1 
    if conts == 1:
        soma1 = (soma1 - dsen) 
        soma2 = (soma2 - dcos)
    else:
        soma1 = (soma1 + dsen)
        soma2 = (soma2 + dcos)
        conts = 0
    cont1 = cont1 + 2 
    cont2 = cont2 + 2 
print (round(soma1,5)) 
print (round(soma2,5))



    
    

