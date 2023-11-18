from random import randint
class BlocoDeNotas:
  def __init__(self):
    self.__notas = list()
  
  def setNotas(self,notas):
    self.__notas = notas
  
  def getNotas(self):
    return self.__notas
    
  def storeNotas(self,notas):
    self.__notas.append(notas)
    
  def numeroDeNotas(self):
    return len(self.__notas)
		
  def showNotas(self,notaNumero):
    if (notaNumero < 0):
      print("Este nao e um numero de nota valido\n")	
    elif (notaNumero < self.numeroDeNotas()):
      print(self.__notas[notaNumero])
    else:
      print("Este nao e um numero de notas valido\n")
    
  def removeNota(self,nota):
    if nota in self.__notas:
      self.__notas.remove(nota)
      print("Nota removida\n")
    else :
      print("Esta nota nao existe\n")
  
  def listaNotasFor(self):
    
    for notas  in self.__notas:
      print(notas)
      
     
  def hasNotas(self):
    if (self.numeroDeNotas() != 0):
      return True
    else:
      return False
      
  def compareNota(self,nota):
    if nota  in self.__notas:
    	return True
    else:
      return False
      
  def showNotaRandom(self,quantas):
    x=0

    while(x < quantas):
      y = randint(0,self.numeroDeNotas())
      x = x+1
      print(self.__notas[int(y)])
               
	
	