import time
import random
import sys
# Dice
def d4():
    return random.randint(1,4)
def d6():
    return random.randint(1,6)
def d8():
    return random.randint(1,8)
def d20():
    return random.randint(1,20)
# Other stuff
def slowPrint(text):
    # take text and print it character by character
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    print("")
