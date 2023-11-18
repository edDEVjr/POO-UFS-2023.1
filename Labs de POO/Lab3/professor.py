class Professor:
	def __init__(self,nome,matriculaSIAPE,cargaHS):
		self.__nome = nome
		self.__matriculaSIAPE = matriculaSIAPE
		self.__cargaHS = cargaHS
	
	def setNome(self,nome):
		self.__nome = nome
	
	def setMatriculaSIAPE(self,matricula):
		self.__matriculaSIAPE = matricula
	
	def setCargaHS(self,cargaHS):
		self.__cargaHS = cargaHS
	
	def getNome(self):
		return self.__nome
	
	def getMatriculaSIAPE(self):
		return self.__matriculaSIAPE
	
	def getCargaHS(self):
		return self.__cargaHS
	
	
	def maisHoras(self,horas):
		self.__cargaHS +=  horas
	
	def menosHoras(self,horas):
		self.__cargaHoras -= horas
	
	