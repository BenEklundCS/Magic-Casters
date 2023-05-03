from player import Player
from monsters import Monster
from functions import slowPrint

def introScene(player, leftCompleted = False, rightCompleted = False, forwardCompleted = False):
    directions = ["left", "right", "forward"]
    slowPrint("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        slowPrint("Options: left/right/backward/forward")
        userInput = input()
        if userInput == "left" and leftCompleted == False:
            showShadowFigure(player)
        elif userInput == "left" and leftCompleted == True:
            slowPrint("You've already gone this way, and there's nothing left to find.")
            introScene(player, True)
        elif userInput == "right":
            showSkeletons() # Not yet defined
        elif userInput == "forward":
            hauntedRoom() # Not yet defined
        elif userInput == "backward":
            slowPrint("You find that this door opens into a wall. Maybe another direction would be better?")
        else: 
            slowPrint("Please enter a valid option for the adventure game.")
            
def showShadowFigure(player):
    slowPrint("You see a shadowy figure in the distance. It is approaching you.")
    slowPrint("What do you do?")
    userInput = ""
    while userInput not in ["run", "fight"]:
        slowPrint("Options: run/fight")
        userInput = input()
        if userInput == "run":
            slowPrint("You run away from the shadowy figure.")
            slowPrint("You find yourself back at the crossroads.")
            introScene()
        elif userInput == "fight":
            slowPrint("You fight the shadowy figure.")
            shadowFight(player)
        else:
            slowPrint("Please enter a valid option for the adventure game.")
            
            
def shadowFight(player):
    monster = Monster("Shadowy Figure", 50, 100, 50, 10, 50)
    userInput = ""
    while userInput not in ["slash", "slam", "pass"]:
        slowPrint("It is your turn to attack.")
        slowPrint("Options: slash/slam/pass")
        userInput = input()
        
        if userInput == "slash":
            player.slash(monster)
        elif userInput == "slam":
            player.slam(monster)
        elif userInput == "pass":
            player.passTurn()
        else:
            slowPrint("Invalid option. Please enter a valid attack!")
            continue
            
        if monster.checkHealth(player) == True:
            del monster
            slowPrint("You also find a key on the shadowy figure's body. Maybe it will be useful later?")
            introScene(player, True, False, False)
        
        monster.defaultAttack(player)
        
        if player.getHealth() <= 0:
            slowPrint("You have lost the battle!")
            gameOver()
        userInput = ""

    return 1
    
def gameOver():
    slowPrint("You have lost! The kingdom is doomed!")
    slowPrint("GAME OVER")
    input()
    exit()
    


