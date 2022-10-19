import art

def cardDealer():
    #this function will be dealing cards.
    import random
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def playerWillDeal():
    playerCards.append(cardDealer())
    
def dealerWillDeal():
    dealerCards.append(cardDealer())
    
    
print(art.logo)

playerCards = []
dealerCards = []
playing = True
#this will give initial cards to player and dealer
playerWillDeal()
dealerWillDeal()

while playing :
    print(playerCards)
    print(dealerCards)
    if (sum(playerCards) or sum(dealerCards)) > 21:
        playing = False
    
    else :
        userChoice = str(input("Enter hit(h) of stand(s) : "))[0].upper()
        if userChoice == "H":
            playerWillDeal()
            continue
        if userChoice == "S":
            while sum(dealerCards) < sum(playerCards):
                dealerWillDeal()
                if sum(dealerCards) > sum(playerCards) and sum(dealerCards) <= 21:
                    print("dealer win")
                
                    
            
    
    