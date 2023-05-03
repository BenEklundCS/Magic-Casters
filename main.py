import time
import sys
from scenes import introScene, showShadowFigure
from player import *
from monsters import *


def main():
  slowPrint("Enter your name:")
  name = input()
  player = Player(name, 100, 100, 30, 10,
                  0)  # name, health, mana, attack, defense
  showShadowFigure(player)


main()
