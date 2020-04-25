#Bruna Ribeiro

def verificaIMC():
    altura = float(input());
    peso = float(input());
    

    imc = peso/(altura*altura);
    
    imc = round(imc, 2);
    
    print(imc)

    if(imc < 17.00):
        print("Muito abaixo do peso");
    elif(imc >=17.0 and imc <18.50):
        print("Abaixo do peso");
    elif(imc >=18.50 and imc < 25.00):
        print("Peso normal");
    elif(imc >=25.0 and imc < 30.00):
        print("Acima do peso");
    elif(imc >=30.0 and imc <35.0):
        print("Obesidade grau I");
    elif(imc >=35.0 and imc<40.0):
        print("Obesidade grau II");
    else:
        print("Obesidade grau III");

    
verificaIMC();
