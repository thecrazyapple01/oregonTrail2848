'''The Oregon Trail BackEnd'''

import sys
import random
import numpy as np

#import the classes and functions libraries
import classes
import functions

#import the blackjack library
import blackjack

#function which closes the program
def ProgramClosing():
    ProgramClosing = input('Press enter to end the program.')
    if ProgramClosing == '':
        print('Closing program...')
        sys.exit()


 #function for when the player reaches the town
 # it prints some messages, lets him know what he can in this new town
 # gets some info (e.g. the prices in the town)
def ActionsInTown(player, checkpoint, prices):
  print("You have reached a new town!")
  print("You only have food left for "\
    ,player.food // foodperday,"days.\n You have energy to travel for another ",player.stamina," days)")
  print("The merchants in this town will sell you some food for ", prices[checkpoint] ,"enemy skalps per unit of food\n")
  print("The following actions are available in this town:\n" \
    "1. Rest (press S) - you regain some stamina. The rent is ",rent[checkpoint],\
      "2. Buy some food - press B")


player = Character() # food, life, daystrav, stamina
townloc = DistancesofCities() #generates the list with town locations from starting point
nbcities = len(townloc)
checkpoint = 0 #the index of the next city visited to be visited
foodperday = 10
prices = PricesInTown(nbcities)
rent = RentInTown(nbcities)

print("You have found an old map! The cities are located at these distances from your location: ")
print("Beware! You are not made of iron. You lose 1 stamina for everyday spent travelling, and you gain 2 stamina back \
  for everyday spent resting in a town along your long way to the Cyborg Dorado.")
print(townloc)

while True:

  if player.DeadPlayer() != 0: #checks if game can continue

    print("Day ", player.dayspassed,". You have travelled so far ",player.daystrav, " days.\n" ,". You have ",player.food\
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
            if amount * prices[checkpoint] <= player.money: # CUM SE POATE ADAUGA VERIFICAREA ASTA LA FUNCTIE OARE?
              player = BuyingFood(foodperday, player, prices, amount)
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
