import numpy as np
import random

def nbcities():
    return random.randint(3, 5) #between 3 and 5 cities

nbcities = nbcities()

#function which returns a random number of cities at random distances
def DistancesofCities(nbcities):
  distances = random.sample(range(2,15), nbcities) #min distance 2 km, max distance 15 km
  distances.sort()
  return np.array(distances).astype(np.int)

#determines the price for food and rent in every town
def PricesInTown(nbcities):
  prices = np.random.normal(25, 8, nbcities)
  return  np.asarray(prices).astype(np.int)

#function to buy food, gets the idx of the city, the price list, the player class
#and the quantity of food the players wants to buy
#returns the player class with modified values for food, money
def BuyingFood(player, checkpoint, prices, amount):
  player.money -= prices[checkpoint] * amount
  player.food += amount 
  
