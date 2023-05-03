# Player class for MagicCasters
from functions import slowPrint, d8, d6
from monsters import Monster

class Player:
    def __init__(self, name, health, mana, attack, defense, gold):
        self.name = name
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.gold = gold
        
    # Setters
    def setName(self, name):
        self.name = name
    def setHealth(self, health):
        self.health = health
    def setMana(self, mana):
        self.mana = mana
    def setAttack(self, attack):
        self.attack = attack
    def setDefense(self, defense):
        self.defense = defense
    def setGold(self, gold):
        self.gold = gold
        
    # Getters
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getMana(self):
        return self.mana
    def getAttack(self):
        return self.attack
    def getDefense(self):
        return self.defense
    def getGold(self):
        return self.gold
    
    # Attacks
    def slash(self, monster):
        slowPrint("You slash the " + monster.getName() + ".")
        roll = d6()
        damage = roll + self.getAttack() - monster.getDefense()
        slowPrint("You rolled a " + str(roll) + " for your slash attack for " + str(damage) + " damage.")
        monster.setHealth(monster.getHealth() - damage)
        slowPrint("The " + str(monster.getName()) + "'s health is now " + str(monster.getHealth()))
        
    def slam(self, monster):
        slowPrint("You slam the " + monster.getName() + " " + str(self.getMana()) + "/100 mana left.")
        self.setMana(self.getMana() - 5)
        roll = d8()
        damage = roll + self.getAttack() - monster.getDefense()
        slowPrint("You rolled a " + str(roll) + " for your slam attack for " + str(damage) + " damage.")
        monster.setHealth(monster.getHealth() - damage)
        slowPrint("The " + str(monster.getName()) + "'s health is now " + str(monster.getHealth()))
        
    def passTurn(self):
        slowPrint("You pass your turn.")
  
    
    
