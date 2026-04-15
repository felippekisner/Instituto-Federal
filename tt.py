from Veiculo import v1, v2, v3

class Pista:
    def __init__(self, extensao, veiculos):
        self.extensao = extensao
        self.veiculos = veiculos

    def __str__(self):
        resultado = f"Extensao da pista: {self.extensao}km\n"
        for i, veiculo in enumerate(self.veiculos, start=1):
            resultado += f"Veiculo {i}: {veiculo}\n"
        return resultado

lista = [v1, v2, v3]

p1 = Pista(80, lista)
print(p1)