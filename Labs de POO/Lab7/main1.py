from catalogo import Catalogo
from cd import Cd
from dvd import Dvd
# criando objetos cds e dvds
cd1 = Cd("Tom",12,"Tais",5,True,"Bom")
cd2 = Cd("jobs",15,"Toby",3,True,"medio")
cd3 = Cd("show",17,"Tulio",2,True,"ok")

dvd1 = Dvd("Carros",120,"Roberto",True,"Bom")
dvd3 = Dvd("DJango",160,"Tarantino",True,"Otimo")
dvd2 = Dvd("It",140,"Stephen King",True,"Bom")

cds = Catalogo()
dvds = Catalogo()

# inserindo cds e dvds
cds.inserirCd(cd1)
dvds.inserirDvd(dvd1)
cds.inserirCd(cd2)
dvds.inserirDvd(dvd2)
cds.inserirCd(cd3)
dvds.inserirDvd(dvd3)
print("Apos a inserção")
print("CDs:")
cds.imprimirCd()
print("DVDs:")
dvds.imprimirDvd()

print("teste localizar:")

if cds.localizarCd(cd2) == True:
  print("Esta na colecao\n")
else:
  print("Não esta na colecao\n")

# removendo cd e dvd
dvds.removerDvd(dvd1)
cds.removerCd(cd1)
print("Apos a remocao")
print("CDs:")
cds.imprimirCd()
print("DVDs:")
dvds.imprimirDvd()



