'''Oregon Trail BackEnd'''

import sys
import random

#function which closes the program
def ProgramClosing():
    ProgramClosing = input('Press enter to end the program.')
    if ProgramClosing == '':
        print('Closing program...')
        sys.exit()

#function which returns a random number of cities at random distances
def DistancesofCities():
  nbcities = random.randint(3, 5) #between 3 and 5 cities
  distances = random.sample(range(2,15), nbcities) #min distance 5 km, max distance 100 km
  distances.sort()
  return distances

class Character:
  def __init__(self, food, life, daystrav, stamina):
    self.food = food
    self.life = life
    self.daystrav = daystrav
    self.stamina = stamina

  def DayPass(self, foodperday):
    self.food -= foodperday #loses some food as a day passes
    return self.food

  def DeadPlayer(self):
    return 0 if player.food or player.stamina == 0 else 1
player = Character(100, 1,0, 10) # the player starts with 100 food and one life (Yolo) in point 0
townloc = DistancesofCities() #generates the list with town locations from starting point
checkpoint = 0 #the index of the next city visited to be visited
dailyfood = 10

print("You have found an old map! The cities are located at these distances from your location: ")
print("Beware! You are not made of iron. You lose 1 stamina for everyday spent travelling, and you gain 2 stamina back \
  for everyday spent resting in a town along your long way to the Cyborg Dorado.")
print(townloc)

while True:
  if player.DeadPlayer() != 0:
    print("Day ", player.daystrav ,". You have ",player.food," food left and ", player.life, "lifepoints. You have already travelled ",player.daystrav\
      ,"days. \n You have stamina to travel for another: ",player.stamina,"days.")
    userInput = input("Press enter to reach a new day ") 
    if userInput == '':
      player.food = player.DayPass(dailyfood) # you need some food to get by
      player.daystrav += 1 #only one day passed
      player.stamina -= 1 #travel is tiring, even in 2848
      if townloc[checkpoint] == player.daystrav:
        print("You have reached a new town!")
        print("Press S if you want to rest here for some time, but beware! You only have food left for "\
          ,player.food // dailyfood,"days")
        userInput = input()
        if userInput == 's' or 'S':
          player.daystrav += 1
          player.stamina += 2 # you get some stamina resting
        player.food += 10 #food collected from the town
        checkpoint += 1 #another town waits for you at the horizon
      if checkpoint == len(townloc):
        print("Congratulations! You have reached your destination!")
        break
  else:
    player.life -= 1
    if player.life == 0:
      print("Your life reached zero. You died. Please desintall this game as you are not worthy to play\
        it ever again. Return to your boring games, loser.")
      break

ProgramClosing()
