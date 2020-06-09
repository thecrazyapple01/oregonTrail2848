import random
import sys
import time

# creates empty deck
deck = [0] * 52 
for i in range(52): #assigns values
    deck[i] = i

#takes the index of a card as a int, returns the name of the card as a string
def name(card_idx): 
    suits = ["diamonds", "hearts", "clubs", "spades"]
    cards = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "jack", "queen", "king"]
    isuit = card_idx // 13
    icard = card_idx % 13
    txt = cards[icard] + " of " + suits[isuit]
    return txt

#takes the index of a card as a int, return the value of the card as an int
def value(card_idx): 
    val = card_idx % 13 + 1 if card_idx % 13 <= 9 else 10 # your code to determine the card value from its index
    val = val + 10 if card_idx % 13 == 0 else val
    return val # Value is a number between 1 and 10

#takes a list with indexes of cards as ints, returns the total value of the hand as an int
def total(hand): 
    tot = 0
    aces = 0
    for i in range(0, len(hand)):
        aces = aces + 1 if hand[i] % 13 == 0 else aces
        tot += value(hand[i])   
    if tot < 21:
        return tot
    if aces != 0 and tot > 21:
        while True:
            if tot > 21 and aces != 0:
                tot = tot - 10
                aces -= 1
            else:
                break
    return tot

#function which computes the total sum of money of game, takes money as a list returns sum as an int
def moneysum(money): 
    sum = 0
    for i in range(len(money)):
        sum += money[i]
    return sum

print("    Blackjack : beat the bank by getting as close to 21 as possible.\n\
Ace can count as 1 or 11 , and jack , queen and king are 10 points")

def blackjack(moneygambled, playersname):

    players = 1
    money = [moneygambled]  # the initial sums of money given to the players 
    windeposit = [0]  #winning deposit (a player can withdraw his/her winnings in this deposit)
        #the game goes on until the money vector is empty (the sum of the vector is zero)
    while moneysum(money) !=0 :
        for j in range(1):
            if money[j] != 0: 
                i = 0  
                hand = [] 
                random.shuffle(deck) #shuffles the deck before each player's round
                stop = False
                while stop == False:  # until S is pressed or total score is over 21 it will add cards from the shuffled deck to the hand       
                    hand.append(deck[i]) 
                    print(playersname, " gets ", name(deck[i]),". ", playersname,"'s hand is worth ", total(hand)," points.")
                    if i == 0: # at the first round you get two cards
                        i += 1
                        hand.append(deck[i]) 
                        print(playersname, " gets ", name(deck[i]),". ", playersname,"'s hand is worth ", total(hand)," points.")
                    if i == 1:  # placing the bet at the first round
                        bet = money[j] + 1
                        while bet > money[j] or bet < 0:    #checking if the bet is valid
                            print(playersname,"current acount is: ", money[j])
                            try:
                                userInput = (input("Place your bet or try your luck next round (i.e. your bet will be zero): ")) #taking the bet
                                if not userInput.isdigit():
                                    stop = True
                                    bet = 0
                                    break
                                bet = int(userInput)
                            except:
                                bet = -1
                        money[j] = money[j] - bet       #taking the bet money from the player's account
                    if total(hand) < 21 and stop == False and bet != 0:
                        i += 1
                        check = input("Draw another card (Enter) or stop giving (’S + Enter’):" )
                        if check == 's' or check == 'S':
                            stop = True
                    else:
                        stop = True
                gameover = False
                score = total(hand)
                if score > 21:  # if player has over 21 points he/she lost the game
                    print("Sorry, ", playersname, " lost.")
                    gameover = True

                if score == 21: # if the player has exactly 21 points he/she won the game
                    if len(hand) != 2:
                        print("Congratulations! ", playersname, " won.")
                        money[j] = money[j] + 2 * bet
                    else:
                        print("Congratulations! ", playersname," has a natural blackjack!")
                        money[j] = money[j] + 2.5 * bet
                    gameover = True
                
                bankhand = []
                bankscore = 0
                while True and gameover == False and bet != 0:  #similar function with creating the hand of the player
                    bankhand.append(deck[i])
                    bankscore = total(bankhand)
                    print("The bank gets ", name(deck[i]),". Its hand is worth ", bankscore," points.") 
                    time.sleep(1)
                    if bankscore <= score: #the bank gets cards until its score is higher than the score of the player
                        i += 1 
                    else:
                        gameover = True 
                if bankscore <= 21 and bankscore > score: #if the bank has a score under 22 and higher than the player it wins the game
                    print("Sorry, ", playersname, " lost.")
                elif score < 21 and bet!= 0:
                    print("Congratulations! ", playersname, " won.")
                    money[j] = money[j] + 2 * bet
                moneymoved = 0
                print("You still have into your playing account an amount of money of: ", money[j])
                if money[j] != 0:
                    while moneymoved > money[j] or moneymoved < 0.1:
                        try:
                            userInput = (input("How much money do you want to withdraw and deposit into your winnings account? ")) #taking the bet
                            if not userInput.isdigit():
                                stop = True
                                bet = 0
                                break
                            moneymoved = int(userInput)
                        except:
                            moneymoved = 0    
                    money[j] -= moneymoved
                    windeposit[j] += moneymoved
                else:
                    print("Sorry, it seems your gambling account is empty and you have to leave the table.")
    print("The gambling account is empty, it seems the game is over.")
    print("This is the money won by every player during the game: ")
    for i in range(1):
        print(playersname,"won ",windeposit,"bucks.")  

    return windeposit[0]



blackjack(120, 'gicu')
