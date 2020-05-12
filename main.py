'''Oregon Trail BackEnd'''

import sys
import random

#function which returns a random number of cities at random distances
def DistancesofCities():
  nbcities = random.randint(3, 5) #between 5 and 15 cities
  distances = random.sample(range(5,100), nbcities) #min distance 5 km, max distance 100 km
  distances.sort()
  return distances

#function which is closes the program
def ProgramClosing():
    ProgramClosing = input('Press enter to end the program.')
    if ProgramClosing == '':
        print('Closing program...')
        sys.exit()

class Character:
  def __init__(self, food, life, kmtrav):
    self.food = food
    self.life = life
    self.kmtrav = kmtrav

  def DayPass(self, foodperday):
    self.food -= foodperday #loses 10 food as a day passes
    return self.food

player = Character(100, 1,0) # the player starts with 100 food and one life (Yolo) in point 0
townloc = DistancesofCities() #generates the list with town locations from starting point
speed = 5 #km per day
days = 1
checkpoint = 0 #the index of the next city visited to be visited


print("You have found an old map! The cities are located at these distances from your location: ")
print(townloc)

while True:
  if player.food != 0:
    print("Day ", days,". You have ",player.food," food left and ", player.life, "lifepoints. You have already travelled ",player.kmtrav," km")
    userInput = input("Press enter to reach a new day ")
    if userInput == '':
      player.food = player.DayPass(10)
      player.kmtrav += speed * 1 #only one day passed
      days += 1
      if checkpoint < len(townloc):
        if townloc[checkpoint] <= player.kmtrav:
          print("You have reached a new town!")
          player.food += 10 #food collected from the town
          checkpoint += 1
        if checkpoint == len(townloc):
          print("Congratulations! You have reached your destination!")
          break
  else:
    player.life -= 1
    if player.life == 0:
      print("Your life reached zero. You died. Please desintall this game as you are not worthy to play\
        it ever again, loser.")
      break

ProgramClosing()
