'''The Oregon Trail BackEnd'''

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

def PricesInTown(nbcities):
  prices = random.sample(range(5,50),nbcities)
  return prices

class Character:
  #atributes of our braves heroes
  def __init__(self, food, life, daystrav, stamina, money):
    self.food = food
    self.life = life
    self.daystrav = daystrav
    self.money = money
    self.stamina = stamina

  #another day passes
  def DayPass(self, foodperday):
    self.food -= foodperday #loses some food as a day passes
    self.stamina -= 1 #traveling is tiring even in 2848
    self.daystrav += 1
    return self

  #checks if players is still alive
  def DeadPlayer(self):
    return 0 if (player.food == 0) or (player.stamina == 0) else 1

  #resting is good for your welbeing
  #increases you stamina, some time passes, you eat some food
  def RestInTown(self, foodperday):
    self.daystrav += 1 #another day passes while resting
    self.stamina  += 3 #stamina regained resting
    self.food -= foodperday
    return self

  def RestInField(self, foodperday):
    self.daystrav += 1 #another day passes while resting
    self.stamina  += 2 #stamina regained resting
    self.food -= foodperday
    return self
  
 #function for when the player reaches the town
 # it prints some messages, lets him know what he can in this new town
 # gets some info (e.g. the prices in the town)
def ActionsInTown(checkpoint, prices):
  print("You have reached a new town!")
  print("Press S if you want to rest here for some time, but beware! You only have food left for "\
    ,player.food // foodperday,"days")
  print("The merchants in this town will sell you some food for ", ,"enemy skalps")

player = Character(100, 1,0, 10) # food, life, daystrav, stamina
townloc = DistancesofCities() #generates the list with town locations from starting point
checkpoint = 0 #the index of the next city visited to be visited
foodperday = 10

print("You have found an old map! The cities are located at these distances from your location: ")
print("Beware! You are not made of iron. You lose 1 stamina for everyday spent travelling, and you gain 2 stamina back \
  for everyday spent resting in a town along your long way to the Cyborg Dorado.")
print(townloc)

while True:
  if player.DeadPlayer() != 0:
    print("Day ", player.daystrav ,". You have ",player.food," food left and ", player.life, "lifepoints. You have already travelled ",player.daystrav\
      ,"days. \n You have stamina to travel for another: ",player.stamina,"days."\
        " You'll reach the next town in: ",townloc[checkpoint] - player.daystrav," days")
    userInput = input("Press enter to reach a new day or if you feel tired you can get some rest by pressing s: ") 
    if userInput == 's' or 'S':
      player = player.RestInField(foodperday)
    if userInput == '':
      player = player.DayPass(foodperday)
      if townloc[checkpoint] == player.daystrav:
        print("You have reached a new town!")
        print("Press S if you want to rest here for some time, but beware! You only have food left for "\
          ,player.food // foodperday,"days")
        print("The merchants in this town will sell you some food for ", ,"enemy skalps")
        userInput = input()
        if userInput == 's' or 'S':
          player = player.RestInTown(foodperday)
        checkpoint += 1 #another town waits for you at the horizon
      if checkpoint == len(townloc):
        print("Congratulations! You have reached your destination!")
        break
  else:
      print("Your life reached zero. You died. Please unintall this game as you are not worthy to play\
        it ever again. Return to your boring games, loser.")
      break

ProgramClosing()
