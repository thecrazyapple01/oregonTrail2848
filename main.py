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

#determines the price for food and rent in every town
def PricesInTown(nbcities):
  prices = random.sample(range(5,50),nbcities)
  return prices

def RentInTown(nbcities):
  prices = random.sample(range(5,50),nbcities)
  return prices

class Character:
  #atributes of our braves heroes
  def __init__(self, food, life, daystrav, stamina, money, dayspassed):
    self.food = food
    self.life = life
    self.daystrav = daystrav
    self.money = money
    self.stamina = stamina
    self.dayspassed = dayspassed

  #another day passes
  def DayPass(self, foodperday):
    self.food -= foodperday #loses some food as a day passes
    self.stamina -= 1 #traveling is tiring even in 2848
    self.daystrav += 1
    self.dayspassed += 1
    return self

  #checks if players is still alive
  def DeadPlayer(self):
    return 0 if (player.food == 0) or (player.stamina == 0) else 1

  #resting is good for your welbeing
  #increases you stamina, some time passes, you eat some food
  def RestInTown(self, foodperday, checkpoint, prices):
    self.dayspassed += 1 #another day passes while resting
    self.stamina  += 3 #stamina regained resting
    self.food -= foodperday
    return self

  #ARE NEVOIE DE ASIGURARE (PROB CEVA TRY EXCEPT) IN CAZUL IN CARE NU ARE DESTUI BANI FRAIERUL
  def RestInField(self, foodperday):
    self.dayspassed += 1 #another day passes while resting
    self.stamina  += 2 #stamina regained resting
    self.food -= foodperday
    return self
  
 #function for when the player reaches the town
 # it prints some messages, lets him know what he can in this new town
 # gets some info (e.g. the prices in the town)
def ActionsInTown(player, checkpoint, prices):
  print("You have reached a new town!")
  print("You only have food left for "\
    ,player.food // foodperday,"days.\n You have energy to travel for another ",player.stamina" days))
  print("The merchants in this town will sell you some food for ", prices[checkpoint] ,"enemy skalps per unit of food\n")
  print("The following actions are available in this town:\n" \
    "1. Rest (press S) - you regain some stamina. The rent is ",rent[checkpoint,\
      "2. Buy some food - press B"])
    return 0

#function to buy food, gets the idx of the city, the price list, the player class
#and the quantity of food the players wants to buy
#returns the player class with modified values for food, money
def BuyingFood(player, checkpoint, prices, amount):
  player.money -= prices[checkpoint] * amount
  player.food += amount 
  return player

player = Character(100, 1,0, 10) # food, life, daystrav, stamina
townloc = DistancesofCities() #generates the list with town locations from starting point
checkpoint = 0 #the index of the next city visited to be visited
foodperday = 10
prices = PricesInTown()
rent = RentInTown()

print("You have found an old map! The cities are located at these distances from your location: ")
print("Beware! You are not made of iron. You lose 1 stamina for everyday spent travelling, and you gain 2 stamina back \
  for everyday spent resting in a town along your long way to the Cyborg Dorado.")
print(townloc)

while True:

  if player.DeadPlayer() != 0: #checks if game can continue

    print("Day ", player.dayspassed". You have travelled so far ",player.daystrav. " days.\n" ,". You have ",player.food\
      ," food left and ", player.life, "lifepoints. You have already travelled ",player.daystrav\
      ,"days. \n You have stamina to travel for another: ",player.stamina,"days."\
        " You'll reach the next town in: ",townloc[checkpoint] - player.daystrav," days")

    userInput = input("Press enter to reach a new day or if you feel tired you can get some rest by pressing s: ") 

    if userInput == 's' or 'S': #resting
      player = player.RestInField(foodperday)

    if userInput == '': #another day passes
      player = player.DayPass(foodperday)
      if townloc[checkpoint] == player.daystrav: # when the player reaches a new town (travels the distance to the new town)
        ActionsInTown(player, checkpoint, prices)
        userInput = input()

        if userInput == 's' or 'S':
          ok = False
          while ok == False:
            if rent[checkpoint] <= player.money:
              player = player.RestInTown(foodperday, checkpoint, prices)
              ok = True # un try except cred CA AR MERGE, dar sunt obosit acum :/

        if userInput == 'b' or 'B':
          ok = False
          while ok == False:
            amount = input("How much food do you want to buy? ")
            if amount * price[checkpoint] <= player.money: # CUM SE POATE ADAUGA VERIFICAREA ASTA LA FUNCTIE OARE?
              player = player.BuyingFood(foodperday, player)
              ok = True #break
            

          
        checkpoint += 1 #we are done with this town, we are going to the next one

      if checkpoint == len(townloc): # the player reaches the destination town
        print("Congratulations! You have reached your destination!")
        break
  else:
      print("Your life reached zero. You died. Please unintall this game as you are not worthy to play\
        it ever again. Return to your boring games, loser.")
      break

ProgramClosing()
