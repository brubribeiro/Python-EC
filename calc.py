#Bruna Ribeiro - 09/05/2020

# Funções da calculadora
def soma(a, b):
    """
    Retorna a soma de a e b (a + b)
    """
    soma = a + b;
    print(a,'+',b,'=',soma);
    calculadora();
    return soma


def subtrai(a, b):
    """
    Retorna a subtração de a por b (a - b)
    """
    sub = a-b;
    print(a,'-',b,'=',sub);
    calculadora();
    return sub


def multiplica(a, b):
    """
    Retorna o produto de a e b (a * b)
    """
    mul = a*b;
    print(a,'x',b,'=',mul);
    calculadora();
    return mul


def divide(a, b):
    """
    Retorna a divisão de a por b (a / b)
    """
    div = (a/b);
    print(a,'/',b,'=',div);
    calculadora();
    return div

def exibe_menu():
    """
    Exibe um menu para o usuário listando as opções 1 para somar,
    2 para subtrair, 3 para multiplicar, 4 para dividir, e 0 para encerrar.
    """
    resposta = int(input('Escolha um número para continuar \n1-Somar \n2-Subtrair \n3-Multiplicar \n4-Dividir \n0-Sair \n'));

    return resposta


def recebe_numeros():
    """
    Pede para o usuário digitar os números para fazer a conta.
    Essa função deve ler e devolver os 2 números lidos (devolva-os como uma tupla).
    Exemplo: return (a, b)

    Para chamar a função, você pode usar:
    x, y = recebe_numeros()
    """
    a = float(input('Digite o primeiro número: '));
    b = float(input('Digite o segundo número: '));

    return (a, b)


def calculadora():
    """
    - Imprime o menu
    - Recebe a opção do usuário
    - Encerra caso o usuário escolha essa opção
    - senão:
        - Recebe os números
        - Realiza a conta de acordo com a opção escolhida
        - Exibe o resultado
        - Recomeça (exibe o menu e recebe a opção)
    """
    resposta = exibe_menu();
    if(resposta == 1):
        a, b = recebe_numeros()
        soma(a,b)
    elif(resposta == 2):
        a, b = recebe_numeros()
        subtrai(a,b)
    elif(resposta == 3):
        a, b = recebe_numeros()
        multiplica(a,b)
    elif(resposta == 4):
        a, b = recebe_numeros()
        divide(a,b)
    elif(resposta == 0):
        print('Fim do programa');
    else:
        print('Opção invalida!');
        calculadora();

# Programa principal (já está pronto, não altere daqui para baixo):
calculadora()
