from Veiculo import Veiculo
class Bicicleta(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo,marchas):
        super().__init__(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.__marchas = marchas
    def setMarchas(self,marchas):
        self.__marchas = marchas
    def getMarchas(self):
        return self.__marchas
    
    def imprimir(self):
        super().imprime()
        print("Numero de Marchas:"+ str(self.__marchas)+"\n")