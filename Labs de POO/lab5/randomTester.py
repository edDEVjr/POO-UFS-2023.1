
import random
class RandomTester:
  def printOneRandom(self):
    print(random.random())

  def printMultiRandom(self,many):
    i=0
    while(i<many):
      print(random.random())
      i=i+1

  def throwDice(self):
    return random.randint(1,7)

  def maxRandom(self,max):
    return random.randint(1,max)

  def minMaxRandom(self,min,max):
    return random.randint(min,max)
  """
  def maxRandom1(self):
    max = self.minMaxRandom(self)
    return random.randint(1,max+1)
  """