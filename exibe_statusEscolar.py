#Bruna Ribeiro

#A
n_aluno = float(input("Digite a nota da aluno: "));
f_aluno = int(input("Digite a quantidade de faltas: "));


def exibe_status(n_aluno,f_aluno):
    if(n_aluno >= 7 and f_aluno <= 25):
        print("Aluno aprovado!");
    elif(n_aluno >= 5 and f_aluno <= 25):
        print("Aluno em recuperação!");
    else:
        print("Aluno reprovado!");

exibe_status(n_aluno,f_aluno);


#B
'''
n_aluno = float(input("Digite a nota da aluno: "));
f_aluno = int(input("Digite a quantidade de faltas: "));

def exibe_status(n_aluno,f_aluno):
    if(n_aluno < 5):
        print("Aluno reprovado!");
    elif(n_aluno >= 7 and f_aluno <= 25):
        print("Aluno aprovado!");
    else:
        print("Aluno em recuperação!");

exibe_status(n_aluno,f_aluno);
'''
