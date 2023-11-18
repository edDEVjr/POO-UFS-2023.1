from item import Item
class Cd(Item):
	def __init__(self,artista,numeroT):
		self.__artista = artista
		self.__numeroT = numeroT

	
	def setArtista(self,artista):
		self.__artista = artista
	def getArtista(self):
		return self.__artista
		
	def setNumeroT(self,numeroT):
		self.__numeroT = numeroT
	def getNumeroT(self):
		return self.__numeroT