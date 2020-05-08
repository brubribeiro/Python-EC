#Bruna Ribeiro

# Escreva a funcao checa_quantidade_divisores(n, qtd) na sequencia:

def checa_quantidade_divisores(n, qtd):
  i = 1
  soma = 0
  while i <= n:
    if n % i == 0:
      soma = soma + 1
      i = i + 1
    else:
      i = i + 1
  
  if qtd == soma:
    return True
  else:
    return False

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
n = int(input())
qtd = int(input())
if checa_quantidade_divisores(n, qtd): # se a funcao devolve True, entao...
	print(n, "possui", qtd, "divisores")
else:
	print(n, "nao possui", qtd, "divisores")
