class NumeroDisplay:
  def __init__(self,limite):
        self.__limite = limite
        self.__valor = 0
  def getLimite(self):
        return self.__limite

  def setLimite(self,limite):
        self.__limite = limite
        
	#/////atvidade 1	
  def getValor(self):
        return self.__valor

  def setValor(self,valor):
        if(self.__limite >= valor):
            self.__valor = valor
	
  def incremento(self):
        self.__valor = (self.__valor+1) % self.__limite
		
  def getNumeroDisplay(self):
        if(self.__valor < 10):
	        return "0" + str(self.__valor)
        else:
            return " "  + str(self.__valor)