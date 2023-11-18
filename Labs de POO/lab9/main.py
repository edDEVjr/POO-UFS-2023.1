
from conta import Conta

sucesso = False
tentativas = 0
maximotenta = 3
print("-----Acessar Conta------")
while not sucesso and tentativas < maximotenta:
	nome = input("\nDigite o nome: ")
	conta = int(input("\nDigite o numero da conta: "))
	try:
		conta1 = Conta(nome,conta)
		sucesso = True
	except ValueError as error:
			print(error)
			print("\nDigite dados validos")
			tentativas +=1
	else:
		pass
	
if(sucesso == False):
	print("\nTentativas excedidas")
	print("\nTente novamente mais tarde")
	exit()


sucesso = False
tentativas = 0
maximotenta = 3
print("----- Area de Deposito-----")
while not sucesso and tentativas < maximotenta:
	valor = int(input("\nDigite o valor de deposito:"))
	try:
		conta1.deposito(valor)
		sucesso = True
	except ValueError as error:
			print(error)
			tentativas +=1
	else:
		pass
if(sucesso == False):
	print("\nNumero de tentativas excedido")
	print("\nTente novamente mais tarde")
	exit()
else:
	print("\n----Deposito realizado-----")
	
sucesso = False
tentativas = 0
maximotenta = 3
print("-----Area de Saque-----")
while not sucesso and tentativas < maximotenta:
	valor = int(input("\nDigite o valor de saque:"))
	try:
		conta1.saque(valor)
		sucesso = True
	except ValueError as error:
			print(error)
			tentativas +=1
	else:
		pass
if(sucesso == False):
	print("\nNumero de tentativas excedido")
	print("\nTente novamente mais tarde")
	exit()
else:
	print("\n-----Saque Realizado------")
	
print('\nProcessos Finalizados')