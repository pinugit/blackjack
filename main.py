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
    
    print("your cards = " +str(playerCards))
    print("dealer cards = " +str(dealerCards))
    
    userChoice = str(input("Enter hit (H) or stand(S): ")).upper()
    
    if userChoice == "H":
        playerWillDeal()
        if sum(playerCards) > 21:
            print("your total is " + str(sum(playerCards)) + " which is greater than 21, \nYou Lost!")
            playing = False
        elif sum(playerCards) == 21:
            print("your cards sum 21 their is no way the dealer is winning")
            playing = False
        else:
            continue
        
    elif userChoice == "S":
        while sum(dealerCards) < sum(playerCards):
            dealerWillDeal()
            
            if (sum(dealerCards) > sum(playerCards)) and (sum(dealerCards) <= 21):        
                print("dealer cards = " +str(dealerCards))
                print("dealer total is " + str(sum(dealerCards)) + " dealer wins!")
                playing = False
                break
            
            elif(sum(dealerCards) > 21):
                print("dealer cards = " +str(dealerCards))
                print("dealer total is " + str(sum(dealerCards)) + " you win!")
                playing = False
                break
            
    elif userChoice == "":
        print("I am seeing you love enter key but please work your little brain and figure out differnt output")
                      
print("program ends")
                    
            
    
    