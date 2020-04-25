#Bruna Ribeiro

def statusEscolar():
    nota = float(input("Digite a nota do aluno: "));
    presenca = float(input("Digite a presença do aluno: "));
    if(nota >= 7 and presenca >= 10):
        print("Aprovado!");
    else:
        print("Reprovado!");


statusEscolar();
