class Cd:
	def __init__(self,titulo,tempoR,artista,numeroT,possuo,comentario):
		self.__titulo = titulo
		self.__tempoR = tempoR
		self.__artista = artista
		self.__numeroT = numeroT
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
	
	def setArtista(self,artista):
		self.__artista = artista
	def getArtista(self):
		return self.__artista
		
	def setNumeroT(self,numeroT):
		self.__numeroT = numeroT
	def getNumeroT(self):
		return self.__numeroT
		
	def setPossuo(self,possuo):
		self.__possuo = possuo
	def getPossuo(self):
		return self.__possuo
		
	def setComentario(self,comentario):
		self.__comentario = comentario
	def getComentario(self):
		return self.__comentario



