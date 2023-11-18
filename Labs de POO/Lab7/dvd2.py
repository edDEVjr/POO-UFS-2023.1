from item import Item
class Dvd(Item):
	def __init__(self,diretor):
		self.__diretor = diretor
		
	def setDiretor(self,diretor):
		self.__Diretor = diretor
	def getDiretor(self):
		return self.__diretor