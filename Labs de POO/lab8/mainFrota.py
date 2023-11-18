from frota import Frota
from mainTransporte import *

veiculo1 = Frota()

veiculo1.inserir(carro1)
veiculo1.inserir(bicicleta2)
veiculo1.inserir(moto1)
veiculo1.inserir(bicicleta1)
veiculo1.inserir(carro2)
veiculo1.inserir(moto2)

print("Veiculos da Frota\n")
veiculo1.imprimirVeiculos()

veiculo1.remover(moto1)
veiculo1.remover(bicicleta2)

print("Veiculos da Frota\n")
veiculo1.imprimirVeiculos()


#teste de verificacao
if(veiculo1.verificar(carro2)):
    print("Esta na frota")
else:
    print('Nao esta na frota')


