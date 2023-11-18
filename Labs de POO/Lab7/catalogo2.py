from cd2 import Cd
from dvd2 import Dvd
class Catalogo:
  
  def __init__(self):
    self.__colecaoItem = list()
  def inserirItem(self,item):
    self.__colecaoItem.append(item)
  def removerItem(self,item):
    if item in self.__colecaoItem:
      self.__colecaoItem.remove(item)
    else:
      print("Esse item nao esta na colecao")
  
  def localizarItem(self,item):
    if item in self.__colecaoItem:
      return True
    else:
      return False
  
  def imprimirItem(self):
    for item in self.__colecaoItem:
      if(type(item) is Cd):
        print("Titulo:",item.getTitulo(),"\nTempoR:",item.getTempoR(),"\nArtista:",item.getArtista(),"\nNumeroT:",item.getNumeroT(),"\nComentario:",item.getComentario(),'\n')
    
    for item in self.__colecaoItem:
      if(type(item) is Dvd):
        print("\nTitulo:",item.getTitulo(),"\nTempoR:",item.getTempoR(),"\nDiretor:",item.getDiretor(),"\nComentario:",item.getComentario(),'\n')
      
	
			
		
	
	

  