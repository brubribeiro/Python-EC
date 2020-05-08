Bruna Ribeiro - 04/05/2020


# Escreva o codigo da funcao le_e_devolve_menor() na sequencia:
def le_e_devolve_menor():
  numero = 0;
  num = 0;
  while numero >= 0:
    numero = int(input());
    if num == 0:
      num = numero;
    if numero <= num and numero >= 0:
       num = numero 
    else:
       num = num
    if num < 0:
      num = 0
  return num

# Escreva o codigo da funcao le_e_devolve_maior() na sequencia:

def le_e_devolve_maior():
  numero = 0;
  num = 0;
  while numero >= 0:
    numero = int(input());
    if numero > num and num >= 0:
      num = numero
    else:
      num = num
  return num


# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input()
if opcao == 'menor':
	menor = le_e_devolve_menor()
	print(menor)
elif opcao == 'maior':
	maior = le_e_devolve_maior()
	print(maior)
