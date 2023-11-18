from carro import Carro
from moto import Moto
from bicicleta import Bicicleta

carro1 = Carro("gvc113","Mercedes",4,"Bens",4)

moto1 = Moto("jsk897","Honda",2,"Titan",150)

bicicleta1 = Bicicleta("lid543","Caloi",2,"Aro29",5)
print("Antes das alteraoces\n")
carro1.imprimir()
moto1.imprimir()
bicicleta1.imprimir()

carro1.setPortas(2)
moto1.setCilindradas(160)
bicicleta1.setMarchas(4)

print("Depois das alteracoes\n")

carro1.imprimir()
moto1.imprimir()
bicicleta1.imprimir()


carro2 = Carro("hdg423","Fiat",4,"Uno",2)

moto2 = Moto("lsd729","Honda",2,"XRE",300)

bicicleta2 = Bicicleta("hbf618","Hurley",2,"Aro26",3)