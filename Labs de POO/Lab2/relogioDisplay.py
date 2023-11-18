from numeroDisplay import NumeroDisplay

class RelogioDisplay:
  def __init__(self):
    self.__horas = NumeroDisplay(24)
    self.__minutos = NumeroDisplay(60)
    self.__segundos = NumeroDisplay(60)
    self.__displayString = "0"
    self.__atualizaTempo()
  
  
  def calculaTempo(self):
    self.__segundos.incremento()
    if(self.__segundos.getValor() == 0):
      self.__minutos.incremento()
      if(self.__minutos.getValor() == 0):
        self.__horas.incremento()
    self.__atualizaTempo()
 	  
	
  
  def __atualizaTempo(self):
	    self.__displayString = (self.__horas.getNumeroDisplay() + ":" + self.__minutos.getNumeroDisplay() + ":" + self.__segundos.getNumeroDisplay())

  def setTempo(self,horas,minutos,segundos):
    self.__horas.setValor(horas)
    self.__horas.setValor(minutos)
    self.__horas.setValor(segundos)
    self.__atualizaTempo()
      
  def getTempo(self):
        return self.__displayString