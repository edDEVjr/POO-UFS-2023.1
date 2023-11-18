class Conta:
	def __init__(self,nome,numeroConta):
		self.setNome(nome)
		self.setNumeroConta(numeroConta)
		self.__saldoDisponivel = 0
		self.__conta = True
		
	def setNome(self,nome):
		if(nome == None):
			raise ValueError("Nenhum nome adicionado")
			return False
		else:
			self.__nome = nome
			return True
			
	def getNome(self):
		return self.__Nome
	
	def setNumeroConta(self,numero):
		if(numero < 0):
			raise ValueError("Valor Invalido")
		else:
			self.__numeroConta = numero
			return True
	def getNumeroConta(self):
		return self.__numeroConta
		
	def setContaAtiva(self,ativa):
		self.__conta = ativa
	def getContaAtiva(self):
		return self.__conta
	
	def setSaldoDisponivel(self,saldo):
		self.__saldoDisponivel = saldo
	def getSaldoDisponivel(self):
		return self.__saldoDisponivel
	
	
	def deposito(self,valor):
		if(valor < 0):
			raise ValueError("Valor Invalido")
		if(not self.__conta):
			raise ValueError("Conta inativa")
		else:
			self.__saldoDisponivel += valor
			return True
	 
	def saque(self,valor):
		if(valor < 0):
			raise ValueError("Valor Invalido")
		if(self.__conta == False):
			raise ValueError("Conta inativa")
		if(valor > self.__saldoDisponivel):
			raise ValueError("Saldo abaixo do valor do saque")
		else:
			self.__saldoDisponivel -= valor
			return True
			