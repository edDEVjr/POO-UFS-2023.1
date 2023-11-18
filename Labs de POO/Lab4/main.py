import os
from blocoDeNotas import BlocoDeNotas

notas1 = BlocoDeNotas()

notas1.setNotas(["Acordar","Escovar os dentes","Tomar banho"]) 

print("-----Notas-----\n")
print(notas1.listaNotasFor())

opcao = opcao = input("Digite a Nota que voce quer adicionar ou -1 para sair\n")
os.system('clear') or None
while(opcao != "-1"):
  notas1.storeNotas(opcao)
  opcao = input("Digite a Nota que voce quer adicionar ou -1 para sair\n")
  os.system('clear') or None
  
os.system('clear') or None

print("Notas Adicionadas")


print("\nNumero de notas:",notas1.numeroDeNotas(),"\n")

print("-----Notas-----\n")
print(notas1.listaNotasFor())

notas1.removeNota(input("Qual nota voce quer remover?\n"))
os.system('clear') or None

print("-----Notas-----\n")
print(notas1.listaNotasFor())


notas1.showNotas(int(input("Qual o indice da nota que voce quer mostrar?\n")))

print("teste hasnotas\n")
if (notas1.hasNotas() == True):
  print("Tem notas\n")
else:
  print("Nao tem notas\n")
   

print("teste compare notas\n")
if(notas1.compareNota(input("Qual nota voce quer comparar?\n"))==True):
  print("Essa nota existe\n")
else:
  print("Essa nota não existe\n")

print("teste showRandom\n")
notas1.showNotaRandom(int(input("Quantas notas voce quer?\n")))


print("-----Notas-----\n")
print(notas1.listaNotasFor())

print("\n--------Fim---------")
