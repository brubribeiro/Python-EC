#Bruna Ribeiro

def imparPar():
    n1 = int(input("Digite o primeiro número: "));
    n2 = int(input("Digite o segundo número: "));
    
    if(n1 % 2 != 0 and n2 % 2 != 0):
        print("Ambos os números são ímpares!");
    elif(n1 % 2 == 0 and n2 % 2 == 0):
        print("Ambos os números são pares!");
    else:
        print("Temos número par e ímpar!");

    if(n1 % n2 == 0):
        print("n1 é multiplo de n2!");
    else:
        print("n1 não é multiplo de n2!");

imparPar();
imparPar();
imparPar();
