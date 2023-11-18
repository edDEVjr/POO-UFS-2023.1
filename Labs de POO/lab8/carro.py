from Veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo,portas):
        super().__init__(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.__portas = portas
    def setPortas(self,portas):
        self.__portas = portas
    def getPortas(self):
        return self.__portas
    
    def imprimir(self):
        super().imprime()
        print("Numero de Portas:"+ str(self.__portas)+"\n")