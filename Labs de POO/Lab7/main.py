from catalogo2 import Catalogo
from cd2 import Cd
from dvd2 import Dvd

# criando objetos cds e dvds
cd1 = Cd("Tais",5)
cd1.setTitulo("Átomos")
cd1.setTempoR(15)
cd1.setPossuo(True)
cd1.setComentario("Bom")

cd2 = Cd("Toby",3)
cd2.setTitulo("Flores")
cd2.setTempoR(12)
cd2.setPossuo(True)
cd2.setComentario("ok")

cd3 = Cd("Tulio",7)
cd3.setTitulo("Dance girl")
cd3.setTempoR(21)
cd3.setPossuo(True)
cd3.setComentario("medio")


dvd1 = Dvd("Mack")
dvd1.setTitulo("Carros")
dvd1.setTempoR(100)
dvd1.setPossuo(True)
dvd1.setComentario("Bom")

dvd2 = Dvd("Tarantino")
dvd2.setTitulo("Django")
dvd2.setTempoR(140)
dvd2.setPossuo(True)
dvd2.setComentario("Otimo")

dvd3 = Dvd("Stephen King")
dvd3.setTitulo("It")
dvd3.setTempoR(120)
dvd3.setPossuo(True)
dvd3.setComentario("ok")

item1 = Catalogo()

# inserindo cds e dvds
item1.inserirItem(cd1)
item1.inserirItem(dvd1)
item1.inserirItem(cd2)
item1.inserirItem(dvd2)
item1.inserirItem(cd3)
item1.inserirItem(dvd3)
print("Apos a inserção")
print("Itens da colecao:")
item1.imprimirItem()

# testando o metodo localizarIten
print("teste localizar:")

if item1.localizarItem(cd2) == True:
  print("Esta na colecao\n")
else:
  print("Não esta na colecao\n")

# removendo cd e dvd da coleção item
item1.removerItem(dvd1)
item1.removerItem(cd1)
print("Apos a remocao\n")
print("Itens da colecao:")
item1.imprimirItem()







