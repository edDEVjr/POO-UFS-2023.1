from relogioDisplay import RelogioDisplay

teste = RelogioDisplay()
x=0
# Rodar relogio
while (x != 2):
  
  print(teste.getTempo())
  teste.calculaTempo()
  print(teste.getTempo())
  x = 0