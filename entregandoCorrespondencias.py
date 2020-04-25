#Bruna Ribeiro

import math

acum = 0
soma = 0

for i in range(1,8):
    num = int(input());
    soma = soma + (num/7)
    if(num >= 100):
        acum = acum + 1

print(acum)
print(math.trunc(soma))


        
