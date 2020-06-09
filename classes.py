class Character:
  #atributes of our braves heroes
  def __init__(self):
    self.food = 100
    self.life = 1
    self.daystrav = 0
    self.money = 200
    self.stamina = 5
    self.dayspassed = 0
    self.foodperday = 10
    
  #another day passes
  def dayPass(self):
    self.food -= self.foodperday #loses some food as a day passes
    self.stamina -= 1 #traveling is tiring even in 2848
    self.daystrav += 1
    self.dayspassed += 1

  #checks if players is still alive
  def deadPlayer(self):
    return 0 if (self.food == 0) or (self.stamina == 0) else 1

  #resting is good for your welbeing
  #increases you stamina, some time passes, you eat some food
  def restInTown(self, foodperday, checkpoint, prices):
    self.dayspassed += 1 #another day passes while resting
    self.stamina  += 3 #stamina regained resting
    self.food -= foodperday

  #ARE NEVOIE DE ASIGURARE (PROB CEVA TRY EXCEPT) IN CAZUL IN CARE NU ARE DESTUI BANI FRAIERUL
  def restInField(self, foodperday):
    self.dayspassed += 1 #another day passes while resting
    self.stamina  += 2 #stamina regained resting
    self.food -= foodperday

  def buyingFood(self, amount):
    player.money -= prices[checkpoint] * amount
    player.food += amount 

  
    