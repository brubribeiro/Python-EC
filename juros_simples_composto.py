#Bruna Ribeiro - 04/05/2020

# Implemente a funcao juros_simples(capital,taxa,tempo) na sequencia:


def juros_simples(capital,taxa,tempo):
  juros = capital * (1+ taxa * tempo)
  return juros

# Implemente a funcao juros_compostos(capital,taxa,tempo) na sequencia:


def juros_compostos(capital,taxa,tempo):
  juros = capital * (1+taxa)**tempo
  return juros

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input()
capital = float(input())
taxa = float(input())
tempo = float(input())
if opcao == 'simples':
	montante_final = juros_simples(capital, taxa, tempo)
elif opcao == 'composto':
	montante_final = juros_compostos(capital, taxa, tempo)
print("{0:.2f}".format(montante_final))
