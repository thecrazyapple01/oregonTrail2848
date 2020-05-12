'''Oregon Trail BackEnd'''

import sys
import random

#function which is closes the program
def ProgramClosing():
    ProgramClosing = input('Press enter to end the program.')
    if ProgramClosing == '':
        print('Closing program...')
        sys.exit()

class Character:
  def __init__(self, food, life):
    self.food = food
    self.life = life

  def DayPass(self):
    self.food -= 10 #loses 10 food as a day passes
    return self.food

player = Character(100, 1)

t = 1

while True:
  if player.food != 0:
    print("Day ", t,". You have ",player.food," food left and ", player.life, "lifepoints.")
    userInput = input("Press enter to reach a new day ")
    if userInput == '':
      player.food = player.DayPass()
      t += 1
  else:
    player.life -= 1
    if player.life == 0:
      print("Your life reached zero. You died. Please desintall this game as you are not worthy to play\
        it ever again, loser.")
      break

ProgramClosing()

