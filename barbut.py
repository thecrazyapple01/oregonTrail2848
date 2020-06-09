import random
import numpy as np

def barbut(moneygambled, playersname):
    players = 1
    money = moneygambled  # the initial sums of money given to the players 
    windeposit = [0]  #winning deposit (a player can withdraw his/her winnings in this deposit)
    
    # the game goes on until the money vector is empty (the sum of the vector is zero)
    while money !=0 :

        # placing the bet at the first round
        bet = money + 1
        while bet > money or bet < 0:    #checking if the bet is valid
            print(playersname,"current acount is: ", money)
            try:
                userInput = (input("Place your bet or try your luck next round (i.e. your bet will be zero): ")) #taking the bet
                if not userInput.isdigit():
                    stop = True
                    bet = 0
                    break
                bet = int(userInput)
            except:
                bet = -1

        dice = np.zeros(2, dtype = int)
        
        for die in range(len(dice)):
            print("Press enter to throw the dice: ")
            inp = input()
            dice[die] = random.randint(1, 6)
            print("The thrown die is: ", dice[die])
        
        value = np.sum(dice)
        if value == 2:
            value = 13 # if you have two ones its better than 6 - 6
        print("The total value of your dice is: ", value)

        # the other guy playing
        diceenemy = np.zeros(2, dtype = int)
        
        for die in range(len(dice)):
            print("Press enter to throw the dice for the other guy: ")
            inp = input()
            diceenemy[die] = random.randint(1, 6)
            print("The thrown die is: ", diceenemy[die])
        
        valueen = np.sum(diceenemy)
        if valueen == 2:
            valueen = 13 # if you have two ones its better than 6 - 6
        print("The total value of the other guy's dice is: ", valueen)
        inp = input()

        if valueen > value:
            print("Sorry, you lost!")
            money -= bet       # taking the bet money from the player's account
        else:
            print("You won!")
            money += bet       # gaining some money
        print("You still have into your playing account an amount of money of: ", money)

        inp = input()

        moneymoved = money + 1
        if money != 0:
            while moneymoved > money or moneymoved < 0.1:
                try:
                    userInput = (input("How much money do you want to withdraw and deposit into your winnings account? ")) #taking the bet
                    if not userInput.isdigit():
                        stop = True
                        bet = 0
                        break
                    moneymoved = int(userInput)
                except:
                    moneymoved = 0    
            money -= moneymoved
            windeposit[0] += moneymoved
        else:
            print("Sorry, it seems your gambling account is empty and you have to leave the table.")

    return windeposit[0]

print("In the end, you won a sum of: ", barbut(100, 'Gigel'))