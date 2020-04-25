#Bruna Ribeiro

import math;

nome1 = input();
idade1 = float(input());
nome2 = input();
idade2 = float(input());
nome3 = input();
idade3 = float(input());
nome4 = input();
idade4 = float(input());
nome5 = input();
idade5 = float(input());

math.fabs(int(idade1));
math.fabs(int(idade2));
math.fabs(int(idade3));
math.fabs(int(idade4));
math.fabs(int(idade5));

print(f"Pessoa: {nome1} , {idade1}");
print(f"Pessoa: {nome2} , {idade2}");
print(f"Pessoa: {nome3} , {idade3}");
print(f"Pessoa: {nome4} , {idade4}");
print(f"Pessoa: {nome5} , {idade5}");

somaidades = idade1+idade2+idade3+idade4+idade5;

print(somaidades);

media_aritmetica = (idade1+idade2+idade3+idade4+idade5)/5;

print(media_aritmetica);

media_geometrica = (idade1*idade2*idade3*idade4*idade5)**(1/5)

print(math.trunc(media_geometrica));
