# Mostrar vagas disponíveis em tempo real. (25 minutos)
import numpy as np

#imaginando que tem 9 vagas, cada elemento é uma vaga
matriz = np.zeros((3,3))

class Vaga:
    is_ocupada = False
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

#vaga tem que ser uma coordenada da matriz
def atualizaVaga(matriz, vaga, bool):
    if bool == True:
        vaga.is_ocupada = True
        matriz[vaga.x][vaga.y] = 1
    else:
        matriz[vaga.x][vaga.y] = 0
        Vaga.is_ocupada = False


#varredura nas vagas para ver disponibilidade
def informaDisponibilidade(matriz):
    disponiveis = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                disponiveis.append(f"{i}{j}")

    print(disponiveis)


#Criação de vagas no sistema
A0 = Vaga(0,0)
A1 = Vaga(0,1)
A2 = Vaga(0,2)
B0 = Vaga(1,0)
B1 = Vaga(1,1)
B2 = Vaga(1,2)
C0 = Vaga(2,0)
C1 = Vaga(2,1)
C2 = Vaga(2,2)


# receberia por sensores
atualizaVaga(matriz, A0, True)
atualizaVaga(matriz, B0, True)
print(matriz)
informaDisponibilidade(matriz)



