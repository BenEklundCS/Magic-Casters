from functions import slowPrint, d4


class Monster:
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

    def checkHealth(self, player):
      if self.getHealth() <= 0:
        slowPrint("You have won the battle! The " + str(self.getName()) + " had " + str(self.getGold()) + " gold on its body.")
        player.setGold(player.getGold() + self.getGold())
        slowPrint("You now have " str(player.getGold()) + " gold!")
        return True
      else:
        return False
      
    def defaultAttack(self, player):
        slowPrint("The " + self.getName() + " attacks you!")
        roll = d4()
        damage = roll + self.getAttack() - player.getDefense()
        slowPrint(str(self.getName()) + " rolled a " + str(roll) + " for " + str(damage) + " total damage.")
        player.setHealth(player.getHealth() - damage)
        slowPrint("Your health is now " + str(player.getHealth()))
