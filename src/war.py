from random import randint

# War.py, a python take on the
# classic card game "War"
# Copyright Finn Lancaster 2021

# Cards in deck: 52
# 3 Classes: Hearts, Spades, Diamonds
# 1-10 for each class
# Jack, Queen, King, and Ace for each class

print("\n Welcome to PyWar, a Python-take on the Classic Card-Game: War")
print("Copyright(c) Finn Lancaster 2021\n\n")

# Pick a random class of card for the user
def randomClass(newClass):
     if newClass == 0:
          classCard = "Hearts"
     elif newClass == 1:
          classCard = "Spades"
     elif newClass == 2:
          classCard = "Diamonds"
     return classCard

# decide whether to serve face card or
# number card
def randomNum():
#face cards are drawn appr. 3/13 of the time
     faceCard = randint(0, 12)
     if faceCard < 9:
          randNum = randint(0, 8)+2
          return randNum
     else:
     # pick a random number, which is mapped
     # to a card following the below key
          randFace = randint(0,3)
          if randFace == 0:
              return "King"
          elif randFace == 1:
              return "Queen"
          elif randFace == 2:
              return "Jack"
          elif randFace == 3:
              return "Ace"

def computerPlayer(computerCard):
     computerClass = randint(0, 2)
     computerClassName = randomClass(computerClass)
     data = "The computer drew a "+ str(computerCard)+" of "+computerClassName
     return str(data)

computerScore = int(0)
playerScore = int(0)
def compareDraws(user, computer, addArg):
    global computerScore, playerScore
    if addArg == "getScores":
        data = "you-"+str(playerScore)+", computer-"+str(computerScore)
        return data
    else:
        computerScr = computer
        userScr = user
        if computer == "Jack":
            computerScr = int(11)
        elif computer == "Queen":
            computerScr = int(12)
        elif computer == "King":
            computerScr = int(13)
        elif computer == "Ace":
            computerScr = int(14)
        if user == "Jack":
            userScr = int(11)
        elif user == "Queen":
            userScr = int(12)
        elif user == "King":
            userScr = int(13)
        elif user == "Ace":
            userScr = int(14)   
        if (userScr > computerScr):
            playerScore = playerScore + 1
            return "You Won! Keep it Up!"
        elif (userScr == computerScr):
            computerScore = computerScore + 1
            playerScore = playerScore + 1
            return  "Tie!"
        elif (userScr < computerScr):
            computerScore = computerScore + 1
            return "The Computer Won! Good Luck Next Game!"   

def nextGame():
    outputResults()

gameNo = 1
def outputResults():
     global gameNo
     userCard = randomNum()
     userClass = randint(0, 2)
     computerCard = randomNum()
     print("Your card is a", userCard, "of", randomClass(userClass))
     print(computerPlayer(computerCard))
     print("\n"+compareDraws(userCard, computerCard, "null"))
     # Each player draws a card, so
     #player+computer = 2 cards. 52/2 is 26
     if gameNo < 26:
         gameNo = gameNo + 1
         inp = input("\nDraw Card? (Y/N)")
         if inp == "Y" or inp == "y":
             nextGame()
         else:
             return
     else:
         data = ("\nThat was the deck. The final score was: "+compareDraws("null", "null", "getScores"))
         print(str(data))

outputResults()
