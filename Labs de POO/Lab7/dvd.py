class Dvd:
	def __init__(self,titulo,tempoR,diretor,possuo,comentario):
		self.__titulo = titulo
		self.__tempoR = tempoR
		self.__diretor = diretor
		self.__possuo = possuo
		self.__comentario = comentario
	
	def setTitulo(self,titulo):
		self.__titulo = titulo
	def getTitulo(self):
		return self.__titulo
		
	def setTempoR(self,tempo):
		self.__tempoR = tempo
	def getTempoR(self):
		return self.__tempoR
	
	def setDiretor(self,diretor):
		self.__diretor = diretor
	def getDiretor(self):
		return self.__diretor
		
	def setPossuo(self,possuo):
		self.__possuo = possuo
	def getPossuo(self):
		return self.__possuo
		
	def setComentario(self,comentario):
		self.__comentario = comentario
	def getComentario(self):
		return self.__comentario
