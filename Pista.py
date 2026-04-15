from Veiculo import *
import time
class Pista:
    def __init__(self,extensao,veiculos):
        self.extensao = extensao
        self.veiculos = veiculos

    def __str__(self):
        resultado = f"Extensao da pista: {self.extensao}km\n"
        for ve in self.veiculos:
            resultado += f"Veiculo {ve}\n"
        return resultado


    def verificar_termino(self):
        for v in self.veiculos:
            if v.odometro <= self.extensao:
                v.andar()
        
    def printar_pista(self):
          for i in self.veiculos:
            d = "_" * int(i.odometro/25)
            print("(",i.odometro,"):",d,i.desenho,"\n")    


lista = [v1,v2,v3]

centralcity = Pista(765,lista)

print(v1.rendimento)
print(v2.rendimento)
print(v3.rendimento)



while True:
    centralcity.verificar_termino()
    centralcity.printar_pista()
    time.sleep(2)
    print("\n______________________________________________________________________________________________________________\n")

    if centralcity.veiculos[0].odometro >= 765 or centralcity.veiculos[1].odometro >= 765 or centralcity.veiculos[2].odometro >= 765:
        break
