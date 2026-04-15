import random
    
class Veiculo:
    def __init__(self, placa, cor,tanque,odometro,rendimento,desenho):
        self.placa = placa
        self.cor = cor
        self.tanque = tanque
        self.odometro = odometro
        self.rendimento = rendimento
        self.desenho = desenho

    def andar(self):
        if self.tanque <= 0:
            return 0
        self.tanque -= 1
        self.odometro += self.rendimento

    def __str__(self):
        return f'''
        Placa:{self.placa}
        Cor:{self.cor}
        Tanque:{self.tanque}
        Odometro:{self.odometro}
        Rendimento:{self.rendimento}
        Desenho:{self.desenho}
        '''
v1 = Veiculo("123-ABC", "verde",30, 0, random.randint(1,50),"o=o")
v2 = Veiculo("321-ABC", "azul",30, 0, random.randint(1,50),"o-o")
v3 = Veiculo("456-ABC", "roxo",30, 0, random.randint(1,50),"o_o")
