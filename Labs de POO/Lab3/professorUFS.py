class ProfessorUFS:
  def __init__(self,nome,matriculaSIAPE,cargaHS):
    self.__nome = nome
    self.__matriculaSIAPE = matriculaSIAPE
    self.__cargaHS = cargaHS
    self.__cargaHSMax = 20
    self.__cargaHSMin = 8
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
    if((self.__cargaHS + horas) <= self.__cargaHSMax ):
      self.__cargaHS +=  horas
    else:
      print("Carga horaria maxima excedida")
    
  
  def menosHoras(self,horas):
    if((self.__cargaHS-horas) >= self.__cargaHSMin):
      self.__cargaHS -= horas
    else:
      print("Nao atingiu a carga horaria minima")
		
		