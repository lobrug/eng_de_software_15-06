# Identificar carros de alunos em vagas de funcionários. (25 minutos)

class Placa_Carro:
    def __init__(self, placa, is_servidor):
        self.placa = placa
        if is_servidor == True:
            self.servidor = True;
        elif is_servidor == False:
            self.servidor = False;

def identifica_servidor(placa_carro):
    if placa_carro.servidor == True:
        print("Estacionado Corretamente")
    elif placa_carro.servidor == False:
        print("Aluno estacionado em vaga de servidor")
    else:
        print("Placa não registrada no sistema")



abc_1234 = Placa_Carro('ABC_1234', False)
abd_1235 = Placa_Carro('ABD_1235', True)

identifica_servidor(abc_1234)
identifica_servidor(abd_1235)