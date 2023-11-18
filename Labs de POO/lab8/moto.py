from Veiculo import Veiculo
class Moto(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo,cilindradas):
        super().__init__(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
        self.__cilindradas = cilindradas
    def setCilindradas(self,cilindradas):
        self.__cilindradas = cilindradas
    def getCilindradas(self):
        return self.__cilindradas
    
    def imprimir(self):
        super().imprime()
        print("Cilindradas:"+ str(self.__cilindradas)+"\n")