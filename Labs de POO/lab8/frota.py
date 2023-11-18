from Veiculo import Veiculo
from carro import Carro
from moto import Moto
from bicicleta import Bicicleta
from mainTransporte import *

class Frota:
    def __init__(self):
        self.__frotaVeiculos = list()
    
    def inserir(self,veiculo):
        if(veiculo not in self.__frotaVeiculos):
            self.__frotaVeiculos.append(veiculo)
            return True
        else:
            return False
    
    def remover(self,veiculo):
        if(veiculo in self.__frotaVeiculos):
            self.__frotaVeiculos.remove(veiculo)
            return True
        else:
            return False
    
    def verificar(self,veiculo):
        if(veiculo in self.__frotaVeiculos):
            return True
        else:
            return False
    
    def imprimirVeiculos(self):
        print("Carros")
        for veiculo in self.__frotaVeiculos:
            if(type(veiculo) is Carro):
                veiculo.imprimir()
        print("Motos")
        for veiculo in self.__frotaVeiculos:
            if(type(veiculo) is Moto):
                veiculo.imprimir()
        print("Bicicletas")
        for veiculo in self.__frotaVeiculos:
            if(type(veiculo) is Bicicleta):
                veiculo.imprimir()
        