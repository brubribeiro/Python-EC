#Bruna Ribeiro

n = int(input("Digite um número: "));
modo = int(input("Escolha um modo: 1- Adição, 2- Multiplicação "));

if(modo < 1 or modo > 2):
        print("Número do modo inválido")

def tabuada(n, modo):
    cont = 1
    soma = 0
    while(cont <= 10):
        if(modo == 1):
            soma = soma + n
            cont = cont + 1
            print(soma)
        else:
             soma = cont * n
             cont = cont + 1
             print(soma)

tabuada(n,modo)
            
    
