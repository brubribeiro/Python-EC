#Bruna Ribeiro

import math;

theta = float(input());
velocidade = float(input());
gravidade = float(input());

radianos = math.radians(theta);
h = (math.pow(velocidade, 2) * (math.sin(radianos))**2)
denominador = (h/(2*gravidade))
     
print(denominador)
